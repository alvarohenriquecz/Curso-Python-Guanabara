"""
Desafio 061: Progressao Aritmetica v2.0

Refaca o desafio 051, lendo o primeiro termo e a razao de uma PA, mostrando
os 10 primeiros termos da progressao usando a estrutura while.
"""

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao
print('\n10 Primeiros Termos da PA com razao {} (Iniciando em {}):'.format(razao, primeiro))
print(primeiro, end=' ')

while primeiro < decimo:
    primeiro += razao
    if primeiro == decimo
        print(primeiro, end='')
    else:
        print(primeiro, end=' - ')
        