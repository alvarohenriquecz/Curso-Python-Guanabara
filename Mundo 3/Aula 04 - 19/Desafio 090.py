"""
Desafio 090: Dicionario em python 

Faca um programa que leia nome e media de um aluno, guardando tambem a situacao em um dicionario.
No final, mostre o conteudo da estrutura na tela.
"""

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
aluno['Situacao'] = 'Aprovado' if aluno['Media'] >= 7 else 'Reprovado'
for k, v in aluno.items():
    print(f'{k} e igual a {v}')
