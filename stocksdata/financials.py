import datetime as dt
from stocksdata.util.ttlcache import daily_cache
from stocksdata.util.get import *

## Basics #########################################################################################################################################

@daily_cache
def annual_balance_sheet(ticker_symbol):
    result = get_json("/stock/financials/balance-sheet/annual-historical", {"ticker_symbol": ticker_symbol})
    for statement in result['annual_historical_balance_sheets']:
        statement['Date'] = dt.datetime.strptime(statement['Date'], '%Y-%m-%d')
    return result.get('annual_historical_balance_sheets')

@daily_cache
def quarterly_balance_sheet(ticker_symbol):
    result = get_json("/stock/financials/balance-sheet/quarterly-historical", {"ticker_symbol": ticker_symbol})
    for statement in result['quarterly_historical_balance_sheets']:
        statement['Date'] = dt.datetime.strptime(statement['Date'], '%Y-%m-%d')
    return result.get('quarterly_historical_balance_sheets')

@daily_cache
def latest_annual_balance_sheet(ticker_symbol):
    result = get_json("/stock/financials/balance-sheet/annual-latest", {"ticker_symbol": ticker_symbol})
    return result.get('current_annual_balance_sheet')

@daily_cache
def latest_quarterly_balance_sheet(ticker_symbol):
    result = get_json("/stock/financials/balance-sheet/quarterly-latest", {"ticker_symbol": ticker_symbol})
    return result.get('current_quarterly_balance_sheet')

@daily_cache
def annual_income_statement(ticker_symbol):
    result = get_json("/stock/financials/income-statement/annual-historical", {"ticker_symbol": ticker_symbol})
    for statement in result['annual_historical_income_statements']:
        statement['Date'] = dt.datetime.strptime(statement['Date'], '%Y-%m-%d')
    return result.get('annual_historical_income_statements')

@daily_cache
def quarterly_income_statement(ticker_symbol):
    result = get_json("/stock/financials/income-statement/quarterly-historical", {"ticker_symbol": ticker_symbol})
    for statement in result['quarterly_historical_income_statements']:
        statement['Date'] = dt.datetime.strptime(statement['Date'], '%Y-%m-%d')
    return result.get('quarterly_historical_income_statements')

@daily_cache
def latest_annual_income_statement(ticker_symbol):
    result = get_json("/stock/financials/income-statement/annual-latest", {"ticker_symbol": ticker_symbol})
    return result.get('current_annual_income_statement')

@daily_cache
def latest_quarterly_income_statement(ticker_symbol):
    result = get_json("/stock/financials/income-statement/quarterly-latest", {"ticker_symbol": ticker_symbol})
    return result.get('current_quarterly_income_statement')


## Income statement line items ####################################################################################################################
"""
def revenue(self, ticker_symbol):
    return latest_annual_income_statement(ticker_symbol).get("Total Revenue", 0.0)

def gross_profit(self, ticker_symbol):
    return latest_annual_income_statement(ticker_symbol).get("Gross Profit", 0.0)
"""

