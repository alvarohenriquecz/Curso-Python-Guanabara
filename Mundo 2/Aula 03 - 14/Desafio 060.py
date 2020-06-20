"""
Desafio 060: Calculo do Fatorial

Faca um programa que leia um numero qualquer e mostre seu fatorial

ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

"""
# Feito com for
numero = int(input('Digite um numero para descobrir seu fatorial:' ))
copia = numero 
resultado = numero
add = ''

for n in range(numero):
    if copia != numero:
        resultado *= copia
    add += str(copia)
    if copia != 1:
        add += ' x '
    copia -= 1

print('{}! = {} = {}'.format(numero, add, resultado))
"""

# Feito com while
numero = int(input('Digite um numero para descobrir seu fatorial: '))
copia = numero
resultado = numero
add = ''

while copia > 0:
    if copia != numero:
        resultado *= copia
    add += str(copia)
    if copia != 1:
        add += ' x '
    copia -= 1

print('{}! = {} = {}'.format(numero, add, resultado))

