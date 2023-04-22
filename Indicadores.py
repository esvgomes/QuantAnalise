######## Novos indicadores ####

import pandas as pd
import numpy as np
import ta

def SuperTrend(	low: pd.core.series.Series,
				high: pd.core.series.Series,
				close: pd.core.series.Series,
				multiplier: int,
				# close: pandas.core.series.Series,
				window: int = 14
				):

	#### ATR = max(High - Low, |Close[-1] - High|, |Close[-1] - Low|)
	ATR = ta.volatility.average_true_range(high=high,low=low,close=close,window=window)

	#### Upper Band = (High Price + Low Price)/2 + multiplier * Average True Range
	#### Lower Band = (High Price + Low Price)/2 – multiplier * Average True Range
	#### Read more: https://blog.earn2trade.com/supertrend-indicator/#ixzz7xudVsx4O
	# print((high.rolling(window, closed='left').max() + low.rolling(window, closed='left').min())/2)
	
	# UpperBand = ((high.rolling(window, closed='left').max() + low.rolling(window, closed='left').min())/2) + (multiplier*ATR.shift(1))
	Upper = ((high.shift(1) + low.shift(1))/2) + (multiplier*ATR.shift(1))
	UpperBand = Upper.rolling(window).min()
	# print('UpperBand')
	# print(UpperBand)
	Lower = ((high.shift(1) + low.shift(1))/2) - (multiplier*ATR.shift(1))
	LowerBand = Lower.rolling(window).max()
	# print('LowerBand')
	# print(LowerBand)
	return [LowerBand,UpperBand]

# #Teste 1 
# #config: multiplier = 2 e window = 3 
# #saida : 	UBand = [na,na,na,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5 ...,19.5]
# #			LBand = [na,na,na,-0.5,0.5,1.5 ... 15.5] 
# print('Inicio teste 1')
# data1 = {'low':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
# 		'high':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
# 		'close':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# 		}
# df1 = pd.DataFrame(data=data1)

# print (df1)

# teste1 = SuperTrend(low = df1.low ,high= df1.high,close= df1.close,multiplier= 2,window= 3)
# df1['STUBand'] = teste1[1]
# df1['STLBand'] = teste1[0]

# print(df1)