import requests


def stock_summary_us(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return : DICT of Company current price, valuations ratios and ranks, summary information

    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/summary').json()
    return response


def historical_stock_financials(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: DICT of Gurufocus Company Financials up to 30 years of annual data and 120 quarters of quarterly data
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/financials').json()
    return response


def stock_key_statistics(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: DICT of Gurufocus selected key ratios and stats
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/keyratios').json()
    return response


def stock_current_quote(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: DICT Response will be an object containing the stock quote data
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/quote').json()
    return response


def historical_ownership(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: DICT of Historical Information about ownership
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/indicator_history').json()
    return response


def current_ownership(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: DICT of Current Institutional Ownership and Insider Ownership Information
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/indicator_history').json()
    return response


def real_time_guru_trades(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: DICT of Real-time Guru stock trades and current holdings data for specific companies
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/gurus').json()
    return response


def real_time_insider_trades(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: DICT of Company Real-time insider trades data
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/insider').json()
    return response


def stock_executives(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: LIST of Get the list of company executives.
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/executives').json()
    return response



def analyst_estimates(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: LIST of Analyst estimate data of a stock.
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/analyst_estimates').json()
    return response


def operating_data(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: LET of Operating data of a stock.
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/operating_data').json()
    return response


def segments_data(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: List of Segments data of a stock.
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/segments_data').json()
    return response


def stock_indicators(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: DICT of stock data of Indicator.
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/stock/indicators').json()
    return response


def stock_news_headlines(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: DICT of Stock News and Headlines
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/stock/indicators').json()
    return response

