"""
DESAFIO 094: Unindo Dicionarios e listas

crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de
cada pessoa em um dicionario e todos os dicionarios em uma lista. No final, mostre:

A) Quantas pessoas cadastradas.
B) A media de idade.
C) Uma lista com mulheres.
D) Uma lista com idade acima da media.
"""

pessoa = dict()
pessoas = list()
media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M?F]: ')).upper().strip()
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    pessoas.append(pessoa.copy())
    continuar = str(input('Quer continuar [S/N]? ')).upper().strip()
    if 'N' in continuar:
        break
print('-=' * 30)
if len(pessoas) == 1:
    leg1 = 'pessoa'
else:
    leg1 = 'pessoas'
print(f'- O grupo tem {len(pessoas)} {leg1}.')
print(f'- A media de idade e de {media / len(pessoas):.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('- Lista das pessoas que estao acima da media: ')
for pes in pessoas:
    if pes['idade'] > media / len(pessoas):
        print()
        for k, v in pes.items():
            print(f'{k.capitalize()} = {v};', end=' ')
print()
print()
print('<< ENCERRADO >> ')
