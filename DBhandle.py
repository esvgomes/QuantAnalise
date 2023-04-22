import pandas as pd
import yfinance as yf
import os

os.chdir(os.path.join(os.getcwd(),"database"))

def atualiza(asset):
		try:
			data = pd.read_csv(asset+".csv")
			
			# print(data.tail())
			data['Date'] = pd.to_datetime(data["Date"])
			
			hoje = pd.Timestamp.date(pd.Timestamp.now())
			ontem = pd.Timestamp.date(hoje - pd.tseries.offsets.DateOffset(days=1))
			ultimoData = pd.Timestamp.date(data.iloc[-1].Date)
			# print(ultimoData)
			
			# 0 segunda ... 6 domingo  Funcao para pegar o ultimo dia util, ainda nao pega feriados
			while (ontem.weekday() > 4):
				ontem = pd.Timestamp.date(ontem - pd.tseries.offsets.DateOffset(days=1))

			# datainternet = pd.read_csv(asset+"atual.csv")
			if (ultimoData != ontem): 
				try:
					print("Coletando yfinance...")
					dataatual = yf.download(asset+".SA",interval = "1d")
					print(dataatual.tail())
					dataatual.to_csv(asset+".csv")
					data = dataatual
					# return 'Atualizado'
				except:
					print('Não conseguiu atualizar o ' + asset + ' no yfinance')
			# return pd.Timestamp.date(data.iloc[-1].Date)
			return 'Atualizado 1'

		except:
			try:
				dataatual = yf.download(asset+".SA",interval = "1d")
				print(dataatual.tail())
				dataatual.to_csv(asset+".csv")
				# return pd.Timestamp.date(dataatual.iloc[-1].Date)
				return 'Atualizado 2'
			except:
				print('Não conseguiu atualizar o ' + asset + ' no yfinance')
				return None

def returnAsset(asset):
	try:
		data = pd.read_csv(asset+".csv")
		return data
	except:
		return (asset + ' nao encontrado')
