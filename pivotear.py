import pandas as pd


# Carrega os dados do arquivo CSV
notas = pd.read_csv('dados/notas.csv')

# Converter as colunas de notas para o tipo float
for unidade in ['Unidade 1', 'Unidade 2', 'Unidade 3', 'Unidade 4', 'Unidade 5']:
    notas[unidade] = notas[unidade].str.replace(',', '.').astype(float)

# Calcular a média das notas, sem prova final
notas['Media'] = notas[['Unidade 1', 'Unidade 2', 'Unidade 3', 'Unidade 4', 'Unidade 5']].mean(axis=1, skipna=True)

notas_pivoteadas = notas.pivot_table(
    index='AlunoID',
    columns='Disciplina',
    values='Media',
    aggfunc='min'
)

print(notas_pivoteadas.head())

notas_pivoteadas.to_csv('dados/notas_pivoteadas.csv', index=False)
