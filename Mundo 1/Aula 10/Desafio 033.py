""" Desafio 033: Maior e Menor valores

Faca um programa que leia tres numeros e mostre 
qual e  o maior valor digitado e o menor valor.
"""
n1 = int(input('Digite o primeiro numero inteiro (ex:10): '))
n2 = int(input('Digite o segundo numero inteiro (ex:15): '))
n3 = int(input('Digite o terceiro numero inteiro (ex: 20): '))
menor = n1
maior = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior  = n3
print('O menor numero e o {} e o maior e o {}!'.format(menor, maior))
