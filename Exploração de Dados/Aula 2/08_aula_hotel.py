#Crie uma tabela de frequência com valores relativos das quantidades de estadias
#Crie um grafico de barras com os valores relativos da posição

import pandas as pd
import matplotlib.pyplot as plt

URL = 'http://harve.com.br/praticas/reservashotel.csv'
dfhotel = pd.read_csv(URL)

# Criar coluna com total de estadias
dfhotel['estadia_total'] = (
    dfhotel['estadias_em_noites_finalsemana']
    + dfhotel['estadias_em_noites_semana']
)

print(dfhotel['estadia_total'])

# Tabela de frequência relativa
frequencia_relativa = (
    dfhotel['estadia_total']
    .value_counts(normalize=True)
    .sort_index()
)

print("Tabela de frequência relativa:")
print(frequencia_relativa)

# Gráfico de barras
plt.figure(figsize=(12,6))

plt.bar(
    frequencia_relativa.index,
    frequencia_relativa.values
)

plt.title('Frequência Relativa das Quantidades de Estadias')
plt.xlabel('Quantidade de Estadias')
plt.ylabel('Frequência Relativa')

plt.show()