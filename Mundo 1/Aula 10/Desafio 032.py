"""
Desafio 032: Ano Bissexto:

faca um programa que leia um ano qualquer e mostre se ele e BISSEXTO.
"""
ano = int(input('Digite um  ano (ex: 1997'))
tam = len(str(ano)) # Atribui a variavel "tam" a quantidade de caracteres que tem o ano digitado
if ano % 4 == 0: # Verifica se o resto da divisao por 4 do ano digitado e igual a 0
    if str(ano)[tam - 1] == '0': # Verifica se o ultimo caractere do ano digitado e 0
        if str(ano)[tam - 2] == '0': # Verifica se o penultimo caractere do ano digitado e igual a 0
            if ano % 400 == 0: # Verifica se o resto da divisao por 400 do ano digitado e igual a 0
                print('{} e um ano bissexto'.format(ano))
            else:
                print('{} nao e bissexto'.format(ano))
        else:
            print('{} nao e bissexto'.format(ano))
    else:
        print('{} nao e bissexto'.format(ano))
else:
    print('{} nao e bissexto'.format(ano))
