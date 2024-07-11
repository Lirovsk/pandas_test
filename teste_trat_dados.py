import json
import pandas as pd
import matplotlib.pyplot as plt

#Leitura e exibição dos dados crus do cartão ordenados pela ordem de leitura
dados = pd.read_json("D:\ hello . txt", lines=True)
print(dados.head())

#Criação e exibição de uma tabela pivot com os dados de temperatura, pressão, aceleração X e aceleração Y
dadosmelted = dados.pivot_table(values= ["temp", "press", "aX", "aY"], index="time")
print(dadosmelted)

#Criação e exibição dos gráficos  relacionados as tabelas pivotadas

print(dadosmelted.plot()) #apenas escreve o tamanho do gráfico no terminal

#Cria gráficos de área para cada uma das colunas da tabela pivotada
axs = dadosmelted.plot.area(figsize=(20,4), subplots=True, stacked=False)

#comando de exibição dos gráficos
plt.show()