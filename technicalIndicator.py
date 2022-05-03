
import pandas as pd
import rsi,MACD
import bollingerBands as bb 

symbols = ['A','AA','AAC','AAN','AAP','AAPL','AAT','ABM','GOOG','MSFT','TSLA','TWTR']
df=pd.read_csv("today_price.csv")

def technicalIndicatorCalc(df):
    
    print(df)
    df.dropna(inplace =True)
    
    #df = pd.read_csv(f"data/{symbol}.csv")
    df= rsi.rsiChecker(df)
    
    df = MACD.macdIndictor(df)
    df = bb.bolingerBandIndicator(df)

    

    df.to_csv(f'finalData/technical.csv',index =False)
    
if '__main__' == __name__:
    technicalIndicatorCalc(df)


# df.join(df1)
# df3 = bollingerBands.bolingerBandIndicator(df).to_frame()
# print(type(df2))
# print(type(df3))
# dfs = [df,df1, df2, df3]
# df_final = reduce(lambda left,right: pd.merge(left,right), dfs)
# dfs = [df1, df2, df3]
# dfs = [df.set_index() for df in dfs]
# df_final=dfs[0].join(dfs[1:])
# df_final.to_csv('A_modified.csv')




