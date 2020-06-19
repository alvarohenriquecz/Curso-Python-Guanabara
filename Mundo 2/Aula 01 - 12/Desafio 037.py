"""
DESAFIO 037: Conversor de Bases Numericas

Escreva um programa que leia u numero inteiro qualquer e peca para o usuario escolher 
a base de conversao:

- 1 para Binario
- 2 para Octal
- 3 para Hexadecimal
"""
num = int(input('Digite um numero inteiro: '))
print('Para qual base voce deseja converter {}?'.format(num))
conv = int(input('Digite 1 para binario, 2 para octal ou 3 para hexadecimal: '))
if conv == 1:
    print('{} em binario e igual a {}'.format(num, bin(num)))
elif conv == 2:
    print('{} em octal e igual a {}'.format(num, oct(num)))
elif conv == 3:
    print('{} em hexadecimal e igual a {}'.format(num, hex(num)))
else:
    print('Valor Invalido! Digite um numero de 1 a 3. ')