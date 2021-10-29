# código de geração do gráfico 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv', sep=',')

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda", palette="tab10")
  grafico.set(title='PREÇO DA GASOLINA POR DIA', xlabel='DIA', ylabel='PREÇO (R$)');

plt.savefig('gasolina.png')