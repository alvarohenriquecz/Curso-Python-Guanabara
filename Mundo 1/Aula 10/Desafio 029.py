""" 
DESAFIO 029: radar eletronico 

escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
"""
vel = int(input('Qual velocidade o carro esta? Digite um numero inteiro (ex: 75)'))
multa = 7.00
total = (vel - 80) * multa
if vel > 80:
    print(' O carro esta a {} Km/h, sendo que a velocidade maxima permitida e 80 Km/h.'.format(vel))
    print('Nesse caso, a multa para ele e de {:.2f}!'.format(total))
else:
    print('O carro esta a {} km/h, portanto esta dentro da velocidade maxima permitida de 80 km/h'.format(vel))
