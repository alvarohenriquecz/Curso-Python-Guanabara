"""
Desafio 049: Tabuada v2.0

Refaca o Desafio 009, mostrando a tabuada de um numero que
o usuario escolher, so que agora utilizando o laco for.
"""

msg = 'Digite um numero para refazer a tabuada desde o 1 ate ele (ex: 10 para fazer a tabuada de 1 ate o 10):'
n = int(input(msg))
print()

for c in range(1, n + 1):
    print('-' * 13)
    print('{}'.format('Tabuada do ' + str(c)))
    print()
    for i in range(1, 10 + 1)
        print('{:<2} x {:>2} = {}'.format(c, i, c * i))
    print('-' * 13)
    print()