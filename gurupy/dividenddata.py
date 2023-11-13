import requests
import pandas as pd
from datetime import date
import gurupy


def dividend_history(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: LIST of 30 years dividend history data of a stock.
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/dividend').json()

    return response


def dividend_history_df(token: str, ticker: str):
    """
    :param token: String of API Token
    :param ticker: String of Stock Ticker
    :return : DataFrame of Dividend History Data
    """
    div_list = dividend_history(token, ticker)
    div_df = pd.DataFrame(div_list)
    div_df.rename(columns={'amount':'Dividend',
                           'ex_date':'ExDate',
                           'record_date':'RecordDate',
                           'pay_date':'PayDate',
                           'type':'DividendType',
                           'currency':'Currency'}, inplace=True)
    div_df['ExDate'] = pd.to_datetime(div_df['ExDate'])
    div_df['Dividend'] = div_df['Dividend'].astype(float)

    return div_df


def dividend_history_exdate_index_df(token: str, ticker: str):
    """
    :param token: String of API Token
    :param ticker: String of Stock Ticker
    :return : DataFrame of Dividend History Data with Index as Ex Div Date
    """
    div_df = dividend_history_df(token, ticker)
    div_df.set_index('ExDate', inplace=True)

    return div_df


def dyt_quarterly_df(token: str, ticker: str ):
    """
    :param token: api key
    :param ticker: stock ticker
    :return: Dividend Yield Theory Dataframe for last 30 years
    """
    div_df = dividend_history_exdate_index_df(token, ticker)
    price_df = gurupy.price_history_date_index_df(token, ticker)
    div_var = 0.0
    div_frequency = 4

    # Trim out special dividends and unused columns
    div_df = div_df.loc[div_df['DividendType'] != 'Special Div.']
    div_df = div_df.drop(['RecordDate', 'PayDate', 'DividendType', 'Currency'], axis=1)

    # Join Price and Dividend Data
    dyt_df = price_df.join(div_df)
    dyt_df['Dividend'].fillna(0, inplace=True)
    dyt_df['DivPay'] = dyt_df['Dividend']

    for index, row in dyt_df.iterrows():
        if row['DivPay'] > 0:
            div_var = row['DivPay']
        else:
            dyt_df.at[index, 'DivPay'] = div_var

    # Trim data set to 30 years
    current_year = date.today().year

    for date_index, row in dyt_df.iterrows():
        if current_year - date_index.year >= 30:
            dyt_df.drop(date_index, inplace=True)

    # Add Fwd Div
    dyt_df['DivPeriod'] = div_frequency
    dyt_df['FwdDiv'] = dyt_df['DivPay'] * div_frequency
    dyt_df['FwdDivYield'] = dyt_df['FwdDiv'] / dyt_df['SharePrice']

    return dyt_df


def dyt_quarterly_aggregate_year_df(token: str, ticker: str ):
    """
    :param token: api key
    :param ticker: stock ticker
    :return: Dividend Yield Theory Dataframe for last 30 years
    """
    dyt_df = dyt_quarterly_df(token, ticker)

    final_df = dyt_df.groupby(dyt_df.index.year).agg(
        {'SharePrice': ['min', 'max', 'mean', 'median'], 'FwdDivYield': ['min', 'max', 'mean', 'median'],
         'Dividend': ['sum']})

    return final_df

