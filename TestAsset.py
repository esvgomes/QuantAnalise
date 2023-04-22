import DBhandle
import Indicadores
import numpy as np
import pandas as pd

#Realiza o backtest em um Asset
def testAsset(Asset):
	data = DBhandle.returnAsset(Asset)
	# print (data.tail())

	################Entrada
	window = 20
	multiplier = 3

	STrend = Indicadores.SuperTrend(low = data.Low ,high= data.High,close= data['Adj Close'] ,multiplier= multiplier,window= window)
	data['STsup'] = STrend[1]


	################Saida
	window = 10
	multiplier = 3

	STrend = Indicadores.SuperTrend(low = data.Low ,high= data.High,close= data['Adj Close'] ,multiplier= multiplier,window= window)
	data['STinf'] = STrend[0]
	
	################Sinais de entrada de compra e saida de compra
	data['Ecompra'] = np.where(data['Adj Close'] > data['STsup'], True, False)
	data['Scompra'] = np.where(data['Adj Close'] < data['STinf'], True, False)
	# print (data.Date.loc(data.Ecompra))

	################ Montando Dataframe final do backtest
	position = 0
	ls_precos_Ecompras = []
	ls_datas_Ecompras = []
	ls_precos_Scompras = []
	ls_datas_Scompras = []

	# print(data.tail())
	for i in range(len(data.index)):
		if i <= window: continue

		# print(i)

		if position == 0 and data['Ecompra'].iloc[i-1] == False and data['Ecompra'].iloc[i] == True:
			position = 1
			ls_precos_Ecompras.append(data['Open'].iloc[i+1])
			ls_datas_Ecompras.append(data['Date'].iloc[i+1])
			# print(i)

		if position == 1 and data['Scompra'].iloc[i-1] == False and data['Scompra'].iloc[i] == True:
			position = 0
			ls_precos_Scompras.append(data['Open'].iloc[i+1])
			ls_datas_Scompras.append(data['Date'].iloc[i+1])

	# print(len(ls_datas_Ecompras),len(ls_datas_Scompras))

	tabela_resultados = pd.DataFrame(zip(ls_datas_Ecompras, ls_precos_Ecompras, ls_datas_Scompras, ls_precos_Scompras), columns=['Data_Ecompra', 'Preco_Ecompra', 'Data_Scompra', 'Preco_Scompra'])
	tabela_resultados['Data_Ecompra'] = pd.to_datetime(tabela_resultados['Data_Ecompra'], errors='ignore')
	tabela_resultados['Data_Scompra'] = pd.to_datetime(tabela_resultados['Data_Scompra'], errors='ignore')

	tabela_resultados['Resultado'] = (tabela_resultados.Preco_Scompra - tabela_resultados.Preco_Ecompra)/tabela_resultados.Preco_Ecompra*100
	# print(tabela_resultados)

	# print('Resultado final = '+ str(tabela_resultados['Resultado'].sum()))
	return(tabela_resultados)