import yfinance as yf
import pandas as pd
df = pd.read_csv("NFTY_26Jun.csv")
print(df[['DATE ','SETTLE PRICE ']])
df =df[['DATE ','SETTLE PRICE ']]
print(df.tail(10))