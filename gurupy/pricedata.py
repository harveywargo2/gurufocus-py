import requests
import pandas as pd


def price_history_sdata(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: LIST of Company historical price/unadjusted price/Full Price/Volume data
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/price').json()
    return response


def price_history_df(token: str, ticker: str):
    """
    :param token: String of API Token
    :param ticker: String of Stock Ticker
    :return : DataFrame of Dividend History Data
    """
    price_list = price_history_sdata(token, ticker)
    price_df = pd.DataFrame(price_list, columns=['Date', 'SharePrice'])
    price_df['Date'] = pd.to_datetime(price_df['Date'])

    return price_df


def price_history_date_index_df(token: str, ticker: str):
    """
    :param token: String of API Token
    :param ticker: String of Stock Ticker
    :return : DataFrame of Dividend History Data
    """
    price_df = price_history_df(token, ticker)
    price_dfa = price_df.set_index('Date')

    return price_dfa

