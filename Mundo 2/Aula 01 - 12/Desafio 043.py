"""
Desafio 043: Indice de Massa Corporal

Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seus status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 ate 30: Sobrepeso
- 30 ate 40: Obsidade
- Acima de 40: Obesidade Morbida
"""

peso = float(input('Digite o seu peso em kg (ex: 80): '))
altura = float(input('Digite o seu peso em m (ex: 1.75): '))
imc = peso / (altura ** 2)
print('Seu IMC e: {:.1}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso!')
elif 18.5 <= imc <= 25:
    print('Voce esta no peso ideal')
elif 25 <= imc < 30:
    print('Voce esta com sobrepeso')
elif 30 <= imc < 40:
    print('Voce esta com obesidade')
elif imc > 40:
    print('Voce esta com obesidade morbida')