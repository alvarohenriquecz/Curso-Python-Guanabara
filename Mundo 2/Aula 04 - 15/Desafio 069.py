"""
Desafio 068: Analise de Dados do Grupo

Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada,
o programa devera perguntar se o usuario quer ou nao continuar. No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos Homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""

sep = '-' * 50
maioresde18 = 0
Homens = 0
mulheresmenos20 = 0
contador = 0
while True:
    print(sep)
    titulo = f'Pessoa Nº {contador + 1}'
    print(f'{titulo:^50}')
    print(sep)
    idade = 'I'
    while sexo != 'M' and sexo != 'F':
        sexo = str(input(f'Sexo [M/F]: '))
        sexo = sexo.strip().upper()[0].replace(' ', '')
    
    if idade > 18:
        maioresde18 += 1
    if sexo == 'M':
        Homens += 1
    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1
    
    contador += 1
    continuar = 'I'
    print(sep)
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer cadastrar outra pessoa [S/N]? '))
        continuar = continuar.strip().upper()[0].replace(' ', '')
    print(sep)
    print('')
    if continuar == 'N':
        break

if contador == 1:
    print('Voce cadastrou somente 1 pessoa. Deste numero,', end=' ')
else:
    print(f'Voce cadastrou {contador} pessoas no total. Deste numero,', end=' ')

if maioresde18 == 0:
    print('nenhum tem mais de 18 anos,', end=' ')
elif maioresde18 == 1:
    print('1 tem mais de 18 anos,' end=' ')
else:
    print(f'{maioresde18} tem mais de 18 anos,', end=' ')

if homens == 0:
    print('nenhum e homem,', end=' ')
elif homens == 1:
    print('1 e homem,', end=' ')
else:
    print(f'{homens} sao homens,'end=' ')

if mulheresmenos20 == 0:
    print('e nenhuma mulher tem menos de 20 anos.')
elif mulheresmenos20 == 1:
    print('e 1 mulher tem menos de 20 anos.')
else:
    print(f'e {mulheresmenos20} mulheres tem menos de 20 anos.')
    