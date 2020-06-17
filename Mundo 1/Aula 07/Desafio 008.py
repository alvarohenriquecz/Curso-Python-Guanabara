""" Desafio 008: Conversor de Medidas
Escreva um programa que leia um valor em metros 
e exiba convertido em contimetros e milimetros
"""

n = int(input('Digite o valor em metros: '))
cm = n * 100
mm = n * 1000
print('{} metro(s) equivalente(m) a {} centrimetros ou a {} milimetros.'.format(n, cm, mm))
