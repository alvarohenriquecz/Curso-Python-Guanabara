"""
Desafio 067: Tabuada v3.0

Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado
pelo usuario, o programa sera interrompido quando o numero solicitado for negativo
"""

sep = '-' * 20
while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    if tabuada < 0 :
        break
    print(sep)
    for n in range(1, 10 + 1)
        print(f'{tabuada} x {n:2} = {tabuada * n}')
    print(sep)
print(sep)
print('Programa tabuada encerrado. volte sempre!')
