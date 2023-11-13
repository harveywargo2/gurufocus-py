import pandas as pd
import requests


def stock_financials(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: DICT of Gurufocus Company Financials up to 30 years of annual data and 120 quarters of quarterly data
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/financials').json()

    return response


def stock_financials_annual_df(token: str, ticker: str):
    """
    Annual Dataframe
    :param token: API Key String
    :param ticker: Stock Ticker String
    :return: Datafram
    """
    df_annual = pd.DataFrame()
    x_loc = 0

    data = stock_financials(token, ticker)
    df_a = pd.DataFrame.from_dict(data)
    df_b = pd.json_normalize(df_a.loc['annuals'])

    for item, values in df_b.items():
        series_expand = pd.Series(values, name=item).explode(ignore_index=True)
        df_series = series_expand.to_frame()
        df_annual = pd.concat([df_annual, df_series], axis=1)
        x_loc += 1

    df_c = df_annual.convert_dtypes()
    final_df = df_c
    return final_df

