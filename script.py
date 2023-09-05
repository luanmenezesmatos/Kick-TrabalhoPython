import pandas as pd
import os

# Criando um dataframe (tabela) através de um arquivo de dados
ies_df = pd.read_csv((os.getcwd() + "/arquivosExcel/CADASTRO_IES_2020.CSV"),
                     encoding='ISO-8859-1', sep=';', low_memory=False)

# Resumo de Visualização de Dados
""" print(ies_df.head()) """