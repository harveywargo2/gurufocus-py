import requests


def stock_summary_us(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Company current price, valuations ratios and ranks, summary information.
    Data Type = DICT
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/summary').json()
    return response


def company_financials(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Gurufocus Company Financials up to 30 years of annual data and 120 quarters of quarterly data.
    Data Type = DICT
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/financials').json()
    return response


def company_key_statistics(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Gurufocus selected key ratios and stats.
    Data Type = DICT
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/keyratios').json()
    return response


def company_current_quote(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Response will be an object containing the stock quote data.
    Data Type = DICT
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/quote').json()
    return response


def historical_close_price(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Company historical price/unadjusted price/Full Price/Volume data.
    Data Type = LIST
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/price').json()
    return response


def historical_ownership(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Historical Information about ownership.
    Data Type = DICT
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/indicator_history').json()
    return response


def current_ownership(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Current Institutional Ownership and Insider Ownership Information.
    Data Type = DICT
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/indicator_history').json()
    return response


def real_time_guru_trades(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Real-time Guru stock trades and current holdings data for specific companies.
    Data Type = DICT
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/gurus').json()
    return response


def real_time_insider_trades(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Company Real-time insider trades data.
    Data Type = DICT
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/insider').json()
    return response


def company_executives(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Get the list of company executives.
    Data Type = LIST
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/executives').json()
    return response


def dividend_history(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Get 30 years dividend history data of a stock.
    Data Type = LIST
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/dividend').json()
    return response


def analyst_estimates(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Get analyst estimate data of a stock.
    Data Type = LIST
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/analyst_estimates').json()
    return response


def operating_data(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Get operating data of a stock.
    Data Type = LIST
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/operating_data').json()
    return response


def segments_data(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Get segments data of a stock.
    Data Type = DICT
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/segments_data').json()
    return response


def stock_indicators(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Get stock data of Indicator.
    Data Type = DICT
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/stock/indicators').json()
    return response


def stock_news_headlines(token: str, ticker: str):
    """
    :param token: API Token String
    :param ticker: Stock Ticker String
    :return: Get stock data of Indicator.
    Data Type = DICT
    """
    response = requests.get(f'https://api.gurufocus.com/public/user/{str(token)}/stock/{str(ticker)}/stock/indicators').json()
    return response

