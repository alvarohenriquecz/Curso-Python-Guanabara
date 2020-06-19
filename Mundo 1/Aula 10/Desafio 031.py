""" 
DESAFIO 031: Custo da viagem 

Desenvolva um programa que pergunte a distancia de uma viagem em km.
Calcule o preco da passagem, cobrando R$ 0,50 por km 
para viagens de ate 200 km e R$ 0,45 para viagens mais longas
"""
distancia = float(input('Digite a distancia em Km da sua viagem (ex: 228.7): '))
if distancia <= 200:
    passagem = distancia * 0.50
    print('Sua passagem para uma viagem de {} km vai custar R$ {:.2f}!'.format(distancia, passagem))
else:
    passagem = distancia * 0.45
    print('Sua passagem para uma viagem de {} Km vai custar R$ {:.2f}!'.format(distancia, passagem))
