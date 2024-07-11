import json
import pandas as pd
import matplotlib.pyplot as plt

#Leitura e exibição dos dados crus do cartão ordenados pela ordem de leitura
dados = pd.read_json("C:\\Users\\Arauj\\OneDrive\\Documentos\\pasta com os dados do sat\\hello . txt" , lines=True)
print(dados.head())

#criação de um pivotado de lat e longitude.
dadospivoted = dados.pivot_table(values=["lat", "long"], index="time")
print(dadospivoted[dadospivoted!=0].dropna())
