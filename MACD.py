#from curses import window
import numpy as np
# import pandas as pd
# import yfinance as yf
# import matplotlib.pyplot as plt


# df.to_csv('tesla.csv')

def macdIndictor(df):
    df['SMA20']= df.CLOSE_PRICE.rolling(window = 20).mean()
    df['SMA50'] = df.CLOSE_PRICE.rolling(window =50).mean()
    df['SMA200'] = df.CLOSE_PRICE.rolling(window =200).mean()
    df['EMA20'] = df.CLOSE_PRICE.ewm(span =20).mean()
    df['EMA50'] = df.CLOSE_PRICE.ewm(span =20).mean()
    df['EMA12']= df.CLOSE_PRICE.ewm(span=12).mean()
    df['EMA26'] = df.CLOSE_PRICE.ewm(span =26).mean()
    df['MACD1'] = df.EMA12- df.EMA26
    df['SIGNAL']= df.MACD1.ewm(span=9).mean()

    #df['MACD'] = np.where(df.MACD1>df.SIGNAL,'UP','Down')

    df['macd_vs_signal']=np.where(df.MACD1>df.SIGNAL,'UP','Down')
    df['50_vs_20ema']=np.where(df.EMA50>df.EMA20,'UP','Down')
    df['20sma_vs_price']=np.where(df.SMA20>df.CLOSE_PRICE,'UP','Down')
    df['50sma_vs_price']=np.where(df.SMA50>df.CLOSE_PRICE,'UP','Down')
    df['200sma_vs_price']=np.where(df.SMA200>df.CLOSE_PRICE,'UP','Down')
    df['ltp']=df['CLOSE_PRICE']

    return df.drop(columns = ['SMA20','SMA50','SMA200','EMA20','EMA50','EMA12','EMA26','MACD1','SIGNAL'])
  