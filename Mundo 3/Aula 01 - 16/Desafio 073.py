"""
Desafio 073: Tuplas com times de futebol

Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do campeonato Brasileiro de futebol, na ordem de colocacao.
Depois mostre:

A) os 5 primeiros.
B) Os ultimos 4 colocados.
C) Times em ordem alfabetica.
D) Em que posicao esta o time da Chapecoence.
"""

div = "-=" * 50
data = '04/06/2018'
times = ('Flamengo', 'Cruzeiro', 'Grêmio', 'São Paulo', 'Internacional',
         'Sport Recife', 'Palmeiras', 'Corinthians', 'Fluminense', 'Atlético',
         'América-MG', 'Botafogo', 'Vasco da Gama', 'Chapecoense', 'Santos',
         'Atlético-PR', 'EC Vitória', 'Bahia', 'Paraná', 'Ceará SC')

print(div)
print(f'Lista de times do Brasileirão ({data}): {times}')
print(div)
print(f'Os 5 primeiros são: {times[:5]}')
print(div)
print(f'Os 4 últimos são: {times[-4:]}')
print(div)
print(f'Times em ordem alfabética: {sorted(times)}')
print(div)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')
