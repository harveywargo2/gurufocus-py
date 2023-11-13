import pandas as pd
import gurupy


def waterfall_stock_cfo_df(token: str, ticker: str):
    annual_df = gurupy.stock_financials_annual_df(token, ticker)
    cash_df = pd.DataFrame(index=annual_df.index)

    cash_df['FiscalYear'] = annual_df[['Fiscal Year']]
    cash_df['Revenue'] = annual_df['income_statement.Revenue'].astype(float)
    cash_df['RevenueGrowth'] = ''
    cash_df['GrossProfit'] = annual_df['income_statement.Gross Profit'].astype(float)
    cash_df['GPM'] = ''
    cash_df['OperatingProfit'] = annual_df['income_statement.Operating Income'].astype(float)
    cash_df['OPM'] = ''
    cash_df['NetProfit'] = annual_df['income_statement.Net Income'].astype(float)
    cash_df['NPM'] = ''
    cash_df['CFO'] = annual_df['cashflow_statement.Cash Flow from Operations'].astype(float)
    cash_df['CfoMargin'] = ''
    cash_df['FCF'] = annual_df['cashflow_statement.Free Cash Flow'].astype(float)
    cash_df['FcfMargin'] = ''
    cash_df['CCE'] = annual_df['balance_sheet.Cash and Cash Equivalents'].astype(float)
    cash_df['MarketSecurities'] = annual_df['balance_sheet.Marketable Securities'].astype(float)
    cash_df['TreasuryStock'] = annual_df['balance_sheet.Treasury Stock'].astype(float)

    return cash_df


def waterfall_reit_ffo_df(token: str, ticker: str):
    annual_df = gurupy.stock_financials_annual_df(token, ticker)
    ffo_df = pd.DataFrame(index=annual_df.index)

    ffo_df['Fiscal Year'] = annual_df[['Fiscal Year']]
    ffo_df['Revenue'] = annual_df['income_statement.Revenue'].astype(float)
    ffo_df['RevenueGrowth'] = ''
    ffo_df['CFO'] = annual_df['cashflow_statement.Cash Flow from Operations'].astype(float)
    ffo_df['CFOMargin'] = ''
    ffo_df['FFO'] = annual_df['cashflow_statement.FFO'].astype(float)
    ffo_df['FFOMargin'] = ''
    ffo_df['FCF'] = annual_df['cashflow_statement.Free Cash Flow'].astype(float)
    ffo_df['FCFMargin'] = ''
    ffo_df['CAPEX'] = annual_df['cashflow_statement.Capital Expenditure'].astype(float)
    ffo_df['CAPEXMargin'] = ''

    return ffo_df


def waterfall_stock_cost_df(token: str, ticker: str):
    annual_df = gurupy.stock_financials_annual_df(token, ticker)
    cost_df = pd.DataFrame(index=annual_df.index)

    cost_df['Fiscal Year'] = annual_df[['Fiscal Year']]
    cost_df['Revenue'] = annual_df['income_statement.Revenue'].astype(float)
    cost_df['COGS'] = annual_df['income_statement.Cost of Goods Sold'].astype(float)
    cost_df['CogsMargin'] = ''
    cost_df['OPEX'] = annual_df['income_statement.Total Operating Expense'].astype(float)
    cost_df['OpexMargin'] = ''
    cost_df['CAPEX'] = annual_df['cashflow_statement.Capital Expenditure'].astype(float)
    cost_df['CapexMargin'] = ''

    return cost_df


def waterfall_stock_debt_df(token: str, ticker: str):
    annual_df = gurupy.stock_financials_annual_df(token, ticker)
    debt_df = pd.DataFrame(index=annual_df.index)

    debt_df['Fiscal Year'] = annual_df[['Fiscal Year']]
    debt_df['Revenue'] = annual_df['income_statement.Revenue'].astype(float)
    debt_df['FreeCashFlow'] = annual_df['cashflow_statement.Free Cash Flow'].astype(float)
    debt_df['TotalCash'] = annual_df['balance_sheet.Cash, Cash Equivalents, Marketable Securities'].astype(float)
    debt_df['CurrentAssets'] = annual_df['balance_sheet.Total Current Assets'].astype(float)
    debt_df['LongAssets'] = annual_df['balance_sheet.Total Long-Term Assets'].astype(float)
    debt_df['CurrentLiabilities'] = annual_df['balance_sheet.Total Current Liabilities'].astype(float)
    debt_df['LongLiabilities'] = annual_df['balance_sheet.Total Long-Term Liabilities'].astype(float)
    debt_df['CurrentRatio'] = ''
    debt_df['ShortDebt'] = annual_df['balance_sheet.Short-Term Debt'].astype(float)
    debt_df['PayOff'] = ''

    return debt_df


def waterfall_reit_debt_df(token: str, ticker: str):
    annual_df = gurupy.stock_financials_annual_df(token, ticker)
    debt_df = pd.DataFrame(index=annual_df.index)

    debt_df['Fiscal Year'] = annual_df[['Fiscal Year']]
    debt_df['Revenue'] = annual_df['income_statement.Revenue'].astype(float)
    debt_df['FFO'] = annual_df['cashflow_statement.FFO'].astype(float)
    debt_df['TotalCash'] = annual_df['balance_sheet.Cash, Cash Equivalents, Marketable Securities'].astype(float)
    debt_df['CurrentAssets'] = annual_df['balance_sheet.Total Current Assets'].astype(float)
    debt_df['LongAssets'] = annual_df['balance_sheet.Total Long-Term Assets'].astype(float)
    debt_df['CurrentLiabilities'] = annual_df['balance_sheet.Total Current Liabilities'].astype(float)
    debt_df['LongLiabilities'] = annual_df['balance_sheet.Total Long-Term Liabilities'].astype(float)
    debt_df['CurrentRatio'] = ''
    debt_df['ShortDebt'] = annual_df['balance_sheet.Short-Term Debt'].astype(float)
    debt_df['PayOff'] = ''

    return debt_df


def waterfall_stock_owner_df(token: str, ticker: str):
    annual_df = gurupy.stock_financials_annual_df(token, ticker)
    owner_df = pd.DataFrame(index=annual_df.index)

    owner_df['Fiscal Year'] = annual_df[['Fiscal Year']]
    owner_df['Revenue'] = annual_df['income_statement.Revenue'].astype(float)
    owner_df['FreeCashFlow'] = annual_df['cashflow_statement.Free Cash Flow'].astype(float)
    owner_df['TotalCash'] = annual_df['balance_sheet.Cash, Cash Equivalents, Marketable Securities'].astype(float)
    owner_df['Dividends'] = annual_df['cashflow_statement.Cash Flow for Dividends'].astype(float)
    owner_df['DivMargin'] = ''
    owner_df['DivGrowth'] = ''
    owner_df['MarketValue'] = annual_df['valuation_and_quality.Market Cap'].astype(float)
    owner_df['RevMultiple'] = ''
    owner_df['MarketGrowth'] = ''
    owner_df['ShareIssues'] = annual_df['cashflow_statement.Issuance of Stock'].astype(float)
    owner_df['ShareBuyBack'] = annual_df['cashflow_statement.Repurchase of Stock'].astype(float)
    owner_df['SharesOutstanding'] = annual_df['income_statement.Shares Outstanding (Diluted Average)'].astype(float)
    owner_df['ShareGrowth'] = ''
    owner_df['OwnerReturn'] = ''
    owner_df['OwnerMargin'] = ''

    return owner_df


def waterfall_reit_owner_df(token: str, ticker: str):
    annual_df = gurupy.stock_financials_annual_df(token, ticker)
    owner_df = pd.DataFrame(index=annual_df.index)

    owner_df['Fiscal Year'] = annual_df[['Fiscal Year']]
    owner_df['Revenue'] = annual_df['income_statement.Revenue'].astype(float)
    owner_df['FundsFromOps'] = annual_df['cashflow_statement.FFO'].astype(float)
    owner_df['TotalCash'] = annual_df['balance_sheet.Cash, Cash Equivalents, Marketable Securities'].astype(float)
    owner_df['Dividends'] = annual_df['cashflow_statement.Cash Flow for Dividends'].astype(float)
    owner_df['DivMargin'] = ''
    owner_df['DivGrowth'] = ''
    owner_df['MarketValue'] = annual_df['valuation_and_quality.Market Cap'].astype(float)
    owner_df['RevMultiple'] = ''
    owner_df['MarketGrowth'] = ''
    owner_df['ShareIssues'] = annual_df['cashflow_statement.Issuance of Stock'].astype(float)
    owner_df['ShareBuyBack'] = annual_df['cashflow_statement.Repurchase of Stock'].astype(float)
    owner_df['SharesOutstanding'] = annual_df['income_statement.Shares Outstanding (Diluted Average)'].astype(float)
    owner_df['ShareGrowth'] = ''
    owner_df['OwnerReturn'] = ''
    owner_df['OwnerMargin'] = ''

    return owner_df


def waterfall_stock_pershare_df(token: str, ticker: str):
    annual_df = gurupy.stock_financials_annual_df(token, ticker)
    ps_df = pd.DataFrame(index=annual_df.index)

    ps_df['FiscalYear'] = annual_df[['Fiscal Year']]
    ps_df['PriceLow'] = annual_df['valuation_and_quality.Lowest Stock Price'].astype(float)
    ps_df['PriceHigh'] = annual_df['valuation_and_quality.Highest Stock Price'].astype(float)
    ps_df['PriceMean'] = ''
    ps_df['Revenue'] = annual_df['per_share_data_array.Revenue per Share'].astype(float)
    ps_df['RevenueGrowth'] = ''
    ps_df['PriceRevenueLow'] = ps_df['PriceLow'] / ps_df['Revenue']
    ps_df['PriceRevenueHigh'] = ps_df['PriceHigh'] / ps_df['Revenue']
    ps_df['EPS'] = annual_df['per_share_data_array.Earnings per Share (Diluted)'].astype(float)
    ps_df['EpsGrowth'] = ''
    ps_df['PriceEarningLow'] = ps_df['PriceLow'] / ps_df['EPS']
    ps_df['PriceEarningHigh'] = ps_df['PriceHigh'] / ps_df['EPS']
    ps_df['FCF'] = annual_df['per_share_data_array.Free Cash Flow per Share'].astype(float)
    ps_df['FcfGrowth'] = ''
    ps_df['PriceFcfLow'] = ps_df['PriceLow'] / ps_df['FCF']
    ps_df['PriceFcfHigh'] = ps_df['PriceHigh'] / ps_df['FCF']

    return ps_df


def waterfall_reit_pershare_df(token: str, ticker: str):
    annual_df = gurupy.stock_financials_annual_df(token, ticker)
    ps_df = pd.DataFrame(index=annual_df.index)

    ps_df['FiscalYear'] = annual_df[['Fiscal Year']]
    ps_df['PriceLow'] = annual_df['valuation_and_quality.Lowest Stock Price'].astype(float)
    ps_df['PriceHigh'] = annual_df['valuation_and_quality.Highest Stock Price'].astype(float)
    ps_df['PriceMean'] = ''
    ps_df['Revenue'] = annual_df['per_share_data_array.Revenue per Share'].astype(float)
    ps_df['RevenueGrowth'] = ''
    ps_df['PriceRevenueLow'] = ps_df['PriceLow'] / ps_df['Revenue']
    ps_df['PriceRevenueHigh'] = ps_df['PriceHigh'] / ps_df['Revenue']
    ps_df['FFO'] = annual_df['per_share_data_array.FFO per Share'].astype(float)
    ps_df['FFOGrowth'] = ''
    ps_df['PriceFFOLow'] = ps_df['PriceLow'] / ps_df['FFO']
    ps_df['PriceFFOHigh'] = ps_df['PriceHigh'] / ps_df['FFO']

    return ps_df


def waterfall_stock_dividend_df(token: str, ticker: str):
    annual_df = gurupy.stock_financials_annual_df(token, ticker)
    div_df = pd.DataFrame(index=annual_df.index)

    div_df['FiscalYear'] = annual_df[['Fiscal Year']]
    div_df['PriceLow'] = annual_df['valuation_and_quality.Lowest Stock Price'].astype(float)
    div_df['PriceHigh'] = annual_df['valuation_and_quality.Highest Stock Price'].astype(float)
    div_df['PriceMean'] = ''
    div_df['Dividend'] = annual_df['per_share_data_array.Dividends per Share'].astype(float)
    div_df['DividendGrowth'] = ''
    div_df['DividendYieldHigh'] = div_df['Dividend'] / div_df['PriceLow']
    div_df['DividendYieldHLow'] = div_df['Dividend'] / div_df['PriceHigh']

    return div_df


def waterfall_reit_dividend_df(token: str, ticker: str):
    annual_df = gurupy.stock_financials_annual_df(token, ticker)
    div_df = pd.DataFrame(index=annual_df.index)

    div_df['FiscalYear'] = annual_df[['Fiscal Year']]
    div_df['PriceLow'] = annual_df['valuation_and_quality.Lowest Stock Price'].astype(float)
    div_df['PriceHigh'] = annual_df['valuation_and_quality.Highest Stock Price'].astype(float)
    div_df['PriceMean'] = ''
    div_df['Dividend'] = annual_df['per_share_data_array.Dividends per Share'].astype(float)
    div_df['DividendGrowth'] = ''
    div_df['DividendYieldHigh'] = div_df['Dividend'] / div_df['PriceLow']
    div_df['DividendYieldHLow'] = div_df['Dividend'] / div_df['PriceHigh']

    return div_df


