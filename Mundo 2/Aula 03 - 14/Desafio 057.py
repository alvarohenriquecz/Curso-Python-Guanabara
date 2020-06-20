"""
Desafio 057: Validacao de Dados

Faca um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'.
Caso esteja errado, peca a digitacao novamente ate ter um valor correto.
"""

sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    print('Valor invalido! Digite M para sexo Masculino ou F para sexo Feminino.')
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
if sexo == 'M':
    print('Voce e do sexo Masculino')
elif sexo == 'F':
    print('Voce e do sexo Feminino')
    