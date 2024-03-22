import streamlit as st
import yfinance as yf
import pandas as pd

# Prepare list of Dow tickers
tickers = ['AXP','AMGN','AMZN','AAPL','BA','CAT','CVS','CSCO','KO','DIS','DOW','GS','HD','HON','INTC','IBM','JNJ','JPM','MCD',
           'MRK','MSFT','NKE','PG','CRM','TRV','UNH','VZ','V','WMT']


frames = []  # Create an empty list to store DataFrames for each ticker

st.title("Dow Jones Industrials comparison of fundamental ratios")

for ticker in tickers:
    fund = yf.Ticker(ticker).info
    frame = pd.DataFrame([fund])
    frames.append(frame)  # Append each ticker's DataFrame to the list


 # Concatenate all DataFrames in the list to display in a single table
result = pd.concat(frames)   
result = result.set_index(['symbol'])

# Calculate EBITDA to Sales ratio
result['ebitdatosales'] = result['ebitda']/result['totalRevenue']

# Populate sector dropdown
sector_dropdown = st.selectbox("Sector",result.sector.unique())
# Populate fundamental dropdown
fundamentals_dropdown = st.selectbox("Fundamentals",['forwardPE','trailingPE','ebitdaMargins','grossMargins','ebitdatosales'])
#Filter data set for viewing
st.text("")
metrics = result[result.sector==sector_dropdown][[fundamentals_dropdown]]

  
# Render output
st.write(result)  
st.text("")
st.text("")
st.header("Dot plot of fundamental values")
st.scatter_chart(metrics,y=fundamentals_dropdown)
