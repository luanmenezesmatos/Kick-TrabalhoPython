import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF

df = pd.read_csv("./arquivosExcel/CADASTRO_IES_2020.CSV", encoding='ISO-8859-1', sep=';', low_memory=False)

df.dropna(inplace=True)

print(df.head())