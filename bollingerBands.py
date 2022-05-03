# import pandas as pd
import  numpy as np 
# import matplotlib.pyplot as plt
# import yfinance as yf

# df = yf.download('MSFT',start= '2021-01-01')
# df.to_csv('MSFT.csv')

def bolingerBandIndicator(df):
    df['SMA']= df['CLOSE_PRICE'].rolling(window = 20).mean()
    #std calculates the standard deviaition
    df['stddev'] = df['CLOSE_PRICE'].rolling(window=20).std()

    df['Upper'] = df['SMA']+2*df['stddev']
    df['Lower'] = df['SMA']-2*df['stddev']

    df['bollinger_price']= np.where(df.Lower>=df.CLOSE_PRICE,'below_lower_band','False')
    df['bollinger_price'] =np.where(df.Upper<=df.CLOSE_PRICE,'above_upper_band',df['bollinger_price'])
    df['bollinger_price'] =np.where((df.Upper>df.CLOSE_PRICE) & (df.Lower<df.CLOSE_PRICE),'between_bands',df['bollinger_price'])
    df.dropna(inplace =True)

    # bollingerCONDITIONS =[
    #     (df.Buy == "True"),
    #     (df.Sell =='True'),
    #     (df.Sell == df.Buy)
    # ]

    # bollingerCATEGORIES= [
    #     'Below Lower band','Above Upper  Band', 'Inbetween Bollingers Band'    
    # ]
    # df['Bollinger Band Signal'] = np.select(bollingerCONDITIONS,bollingerCATEGORIES)
    return df.drop(columns =['SMA','stddev','Upper','Lower'])







