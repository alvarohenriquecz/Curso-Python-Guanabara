"""
Desafio 042: Analisando Trangulos v2.0

Refaca o Desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:

- Equilatero: todos os lados iguais
- Isoceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r1 == r3:
        print('Os segmentos acima podem formar um triangulo equilatero')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
        print('Os segmentos acima podem formar um triangulo isoceles!')
    else:
        print('Os segmentos acima podem formar um triangulo escaleno')
else:
    print('Os segmentos acima nao podem formar um triangulo')

