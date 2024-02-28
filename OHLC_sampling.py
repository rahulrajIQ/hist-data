import pandas as pd
from datetime import date
import calendar



def sampling(df): 
 
    ohlc_dict = {'open' : 'first', 'high' : 'max', 'low' : 'min', 'close' : 'last'}  
    df_sample = df.resample('15Min').apply(ohlc_dict).dropna(how='any')  
    
    return df_sample

df= pd.read_csv('NIFTY_BANK.csv', parse_dates=['timestamp'], 
    date_parser=lambda x: pd.to_datetime(x, format='%d-%m-%Y %H:%M'))

df = df.set_index('timestamp')
df_sample = sampling(df)
df_sample.to_csv('NiftyBank_15m.csv')

