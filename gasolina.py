# código de geração do gráfico
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


gasolina_df = pd.read_csv('gasolina.csv' ,delimiter=',')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda', marker='o')
  grafico.set_xticks(gasolina_df['dia'])
  grafico.set_title('Preço médio de venda da gasolina na cidade de São Paulo', fontweight='bold')
  grafico.figure.set_size_inches(w=(18 / 2.54), h=(15 / 2.54))
plt.show()
grafico.figure.savefig(fname='gasolina.png', bbox_inches='tight')