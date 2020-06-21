"""
Desafio 083: Validando expressoes matematicas

Crie um programa onde o usuario digite uma expressao qualquer que use parenteses. Seu aplicativo devera
analisar se a expressao passada esta com os parenteses abertos e fechados na ordem correta.
"""
par1, par2 = list(), list()
expressao = str(input('Digite a expressao: '))
for caractere in expressao:
    if '(' in caractere:
        par1.append(caractere)
    if ')' in caractere:
        par2.append(caractere)

if len(par1) == len(par2):
    print('Sua expressao esta valida!')
else:
    print('Sua expressao esta errada!')
