"""
Desafio 027: Primeiro e ultimo Nome de uma Pessoa

Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida 
o primeiro e o ultimo nome separadamente
Ex: Ana Maria de Souza
primeiro : Ana
ultimo = Souza
"""

nome = input('Digite seu nome completo: ').strip().split()
qtd = len(nome)
print('\nSeu primeiro nome e {} e seu ultimo nome e {}!'.format(nome[0], nome[qtd-1]))

