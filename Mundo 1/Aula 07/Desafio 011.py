""""
DESAFIO 001: Pintando Parede

Faca um programa que leia a largura e a altura de uma parede 
em metros, Calcule a sua quantidade de tinta necessaria para pinta-la
sabendo que cada litro de tinta, pinta uma area de 2m^2.
"""

l = float(input('Digite a  largura da parede, em metros: '))
a = float(input('Digite a altura da parede, em metros: '))
t = 2
m2 = l * a
r = m2 / t
print('/nA area das paredes de {:.2f}m x {:.2f}m e {:.2f}m^2, e sera necessario comprar'.format(l, a, m2), end=' ')
print('{:.2f} litro(s) de tinta para pintar tudo!'.format(r))
