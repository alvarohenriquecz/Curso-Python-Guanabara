"""
Desafio 048: Soma Impares Multiplos de Tres

faca um programa que calcule a soma entre todos os numeros impares que
sao multiplos de tres e que se encontram no intervalo de 1 ate 500.
"""
t = 0
print('Todos os numeros impares que sao multiplos de 3 e estao entre 1 e 500')
for c in range(1, 500 + 1, 2):
    if c % 3 == 0:
        print(c, end=' ')
        t += c
print('\nSOMA DE TODOS: {}'.format(t))
