"""
Desafio 092: Cadastro  de trabalhador em python

crie um programa que leia nome, ano de nascimento e carteira de trabalho e o cadastre-os (com idade) em um dicionario
se por acaso a CTPS for diferente de ZERO, o dicionario recebera tambem o ano de contratacao e o salario.
calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import datetime
ano_atual = datetime.now().year
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = ano_atual - int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratacao: '))
    pessoa['salario'] = float(input('salario: R$'))
    pessoa['aposentadoria'] = (pessoa['contratacao'] + 35) - (ano_atual - pessoa['idade'])
print('-=' * 30)
for k, v in pessoa.items():
    if k == 'ctps':
        print(f'{k.upper()} tem o valor {v}')
    else:
        print(f'{k.capitalize()} tem o valor {v}')
