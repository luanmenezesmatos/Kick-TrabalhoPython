import pandas as pd
import os

""" df = pd.read_csv("./arquivosExcel/CADASTRO_IES_2020.CSV",
                 encoding='ISO-8859-1', sep=';', low_memory=False)

df.dropna(inplace=True)

print(df.head()) """

# Criando um dataframe (tabela) através de um arquivo de dados
ies_df = pd.read_csv((os.getcwd() + "/arquivosExcel/CADASTRO_IES_2020.CSV"), encoding='ISO-8859-1', sep=';', low_memory=False)

# Resumo de Visualização de Dados
print(ies_df.head(10))  # Mostra as 10 primeiras linhas
print(ies_df.shape)  # Mostra a quantidade de linhas e colunas
print(ies_df.columns)  # Mostra o nome das colunas
print(ies_df.dtypes)  # Mostra o tipo de dado de cada coluna
print(ies_df.info())  # Mostra o resumo das colunas
print(ies_df.describe())  # Mostra um resumo estatístico das colunas numéricas
print(ies_df['CO_IES'].value_counts())  # Mostra a quantidade de valores únicos
print(ies_df.tail(10))  # Mostra as 10 últimas linhas