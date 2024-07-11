import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Leitura e exibição dos dados crus do cartão ordenados pela ordem de leitura
dados = pd.read_json("C:\\Users\\Arauj\\OneDrive\\Documentos\\pasta com os dados do sat\\hello . txt" , lines=True)
print(dados.head())

#criação de um pivotado de lat e longitude.
dadospivoted1 = dados.pivot_table(values=["lat", "long"], index="time")

print("Dados diferentes de zero oriundos do pivotado de alt e long \n")
print(dadospivoted1[dadospivoted1!=0].dropna())

#criação de um pivotado para as acelerações
dadospivoted2 = dados.pivot_table(values=["aX", "aY", "aZ"], index="time")
print("dados de acelarção iguais a zero dentro do tempo de gravação dos daddos \n")
print(dadospivoted2[dadospivoted2==0].dropna())
print("daddos de aceleraççao diferentes de zero: \n")
print(dadospivoted2[dadospivoted2!=0].dropna())

#criação de um pivotado com todos os sensores de gases para ver se houve alguma captação de dados
gases = ("alc","tol","NH4","ace","co","eco2", "co2")
for gas in gases:
    print(dados)

#criação de um pivotado apenas com o valoe de eco2
dadospivoted4 = dados.pivot_table(values=["eco2"], index="time")
print("dados de eco2 \n")
print(dadospivoted4[dadospivoted4!=0].dropna())