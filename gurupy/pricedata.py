import gurupy as gf
import pandas as pd


def historical_price_dataframe(token: str, ticker: str):
    """
    :param token: String of API Token
    :param ticker: String of Stock Ticker
    :return : DataFrame of Dividend History Data
    """
    price_list = gf.historical_close_price(token, ticker)
    price_df = pd.DataFrame(price_list)
    price_df.columns = ['Date', 'SharePrice']
    price_df['Date'] = pd.to_datetime(price_df['Date'])

    return price_df

