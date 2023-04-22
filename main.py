print("Pragrama Inicio")

import DBhandle
import Constantes
import Indicadores
import numpy as np
import pandas as pd
import TestAsset

#Testar Entreda Supertrend(window = 20, multiplier = 3) Saida: Supertrend(window = 10, multiplier = 3)

ls_backtest = []

Asset = ['PRIO3','RRRP3']

for papel in Asset:
	tabela = TestAsset.testAsset(papel)

	# print(tabela.tail())
	print('Resultado final '+ papel + ' = ' + str(tabela['Resultado'].sum()))

	ls_backtest.append([papel,tabela])

print(ls_backtest[0][0])
data1 = ls_backtest[0][1]
data2 = ls_backtest[1][1]

data1.to_csv(ls_backtest[0][0] + 'backtest.csv')
data2.to_csv(ls_backtest[1][0] + 'backtest.csv')

print(data1[data1.Data_Ecompra == pd.to_datetime('2013-12-19')])
# print(str(data1.iloc[1,0]))

#Falta montar o backtest misturando os dois papeis

dataInicial = pd.to_datetime('2010-01-01')
dataFinal = pd.to_datetime('2024-01-01')
step = dataInicial
print('step = ' + str(step))
print('final = ' + str(dataFinal))
print(step < dataFinal)
backtest = []
i=0
j=0



while (step<dataFinal):
	if data1.iloc[i,0] == step and :#Fazer o and para entrar apenas se for menor que o len(data1)
		backtest.append([ls_backtest[0][0],data1.iloc[i]])
		j=1
	if data2.iloc[i,0] == step:
		backtest.append([ls_backtest[1][0],data2.iloc[i]])
		j=1

	if j==1:
		i+=1
		j=0

	step += pd.tseries.offsets.DateOffset(days=1)
	print(step) 

print(backtest)

# 			data['Date'] = pd.to_datetime(data["Date"])
			
# 			hoje = pd.Timestamp.date(pd.Timestamp.now())
# 			ontem = pd.Timestamp.date(hoje - pd.tseries.offsets.DateOffset(days=1))
# 			ultimoData = pd.Timestamp.date(data.iloc[-1].Date)
# 			# print(ultimoData)






################## Atualiza 1 papel ####

# tentativa = DBhandle.atualiza('RRRP3')
# print('Tentativa = ' + str(tentativa))


################## Atualiza todos os paepeis ####

# erro = []

# for asset in Constantes.BRXX:
# 	print('Baixando ' + asset + ' ...')
# 	try:
# 		tentativa = DBhandle.atualiza(asset)
# 		print(asset + ' = ' + str(tentativa))
# 		if tentativa == None: erro.append(asset)
# 	except:
# 		erro.append(asset + ' execpt')

# print(erro)

################## Captura 1 papel do database ####

# data = DBhandle.returnAsset('RRRP3')
# print (data.tail())

# STrend = Indicadores.SuperTrend(low = data.Low ,high= data.High,close= data['Adj Close'] ,multiplier= 3,window= 14)

# data['STinf'] = STrend[0]
# data['STsup'] = STrend[1]
# print (data.tail(18))

