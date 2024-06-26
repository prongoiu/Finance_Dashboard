#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import yfinance as yf
import json

ticker_symbol = input("Enter the ticker symbol: ")

stock = yf.Ticker(ticker_symbol)

pe_ratio = stock.info['trailingPE']
net_profit_margin = stock.info['profitMargins']
debt_to_equity = stock.info['debtToEquity']

ratios = {
    "Price-to-Earnings (P/E) ratio": pe_ratio,
    "Net Profit Margin": net_profit_margin,
    "Debt-to-Equity (D/E) ratio": debt_to_equity
}

json_string = json.dumps(ratios, indent=4)

print(json_string)

