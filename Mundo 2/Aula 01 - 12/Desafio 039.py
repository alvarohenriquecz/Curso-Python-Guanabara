"""
Desafio 029: Alistamento Militar

Faca um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade ,
se ele ainda vai se alistar ao servico militar, se e a hora de e alistar, ou se ja passou
do tempo do alistamento. Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
atual = date.today().year
genero = str(input('Voce e homem ou mulher? Digite H para HOMEM e M para MULHER: ')).upper().strip()
if genero == 'H':
    nas = int(input('Em que ano voce nasceu (ex: 1999)? '))
    ani = str(input('Este ano voce ja fez aniversario? Digite S para SIM e N para NAO: ')).upper().strip()
    if ani == 'N' or ani == 'NAO' or ani == 'NÃO':
        idade = atual - nas - 1
    else:
        idade = atual - nas 
    print('Entao voce tem {} anos, correto?'.format(idade))
    if idade == 18:
        print('Este ano voce deve se alistar no servico militar!')
    elif idade < 18:
        print('Ainda falta(m) {} ano(s) para voce se alistar no servico militar !'.format(18 - idade))
    elif idade > 18:
        print('Ja passou {} ano(s) do tempo para voce se alistar no servico militar!'.format(idade -18))
elif genero == 'M':
    print('Como voce e mulher, nao precisara se alistar no servico militar!')
else: 
    print('Escolha invalida! Tente novamente.')
