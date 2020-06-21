"""
Desafio 077: Contando vogais em tupla

crie um programa que tenha uma tupla com varias palavras (nao usar acentos).
Depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais.
"""

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
vogais = 'aeiou'

for p in palavras:
    v = ''
    for letra in p:
        if letra in vogais:
            v += ' ' + letra
    
    print(f'Na palavra {p.upper()} temos as vogais: {v}')
    