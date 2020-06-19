""" Desafio 024: Verificando as primeiras letras de um texto

Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "SANTO"

"""
cidade = input('Digite o nome da cidade: ')
cl = cidade.upper().strip().split()
res = cl[0] == 'SANTO'
print('\nA cidade comeca ou nao com a palavra "Santo"? True significa Sim e False signifia que nao')
print('Resposta: {}'.format(res))
