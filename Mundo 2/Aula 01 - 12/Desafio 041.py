"""
DESAFIO 041: Classificando Atletas

A confederacao Nacional de Natacao precisa de um programa que leia o ano
de nascimente de um atleta e mostre sua categoria, de acordo com a idade:

- ate 9 anos : mirin
- ate 14 anos : infantil
- ate 19 anos : junior
- ate 25 anos : senior
- acima : master
"""
from datetime import date
atual = data.today().year
nas = int(input('Em que ano o atleta nasceu (ex: 1990)? '))
ani = str(input('Este ano o atleta ja fez aniversario? Digite s para sim e n para nao: ')).upper().strip()
if ani == 'N' or ani == 'NAO' or ani == 'NÃO':
    idade = atual - nas - 1
else:
    idade = atual - nas
if idade <= 9:
    print('O atleta de {} anos vai ficar na categoria MIRIN'.format(idade))
elif idade <= 14:
    print('O atleta de {} anos vai ficar na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta de {} anos vai ficar na categoria JUNIOR'.format(idade))
elif idade <= 25:
    print('O atleta de {} anos vai ficar na categoria SENIOR'.format(idade))
elif idade > 25:
    print('O atleta de {} anos vai ficar na categoria MASTER'.format(idade))
    