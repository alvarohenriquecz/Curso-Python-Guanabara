"""
Desafio 072: Numero por extenso

Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte.
Seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso.
"""

numero = int(input('Digite um número entre 0 e 20: '))
nome = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while numero not in range(0, 20 + 1):
    numero = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
print(f'Voce digitou o numero {nome[numero]}.')
