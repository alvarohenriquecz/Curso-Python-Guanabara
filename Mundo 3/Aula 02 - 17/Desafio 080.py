"""
Desafio 080: Lista Ordenada sem Repeticoes

Crie um programa onde o usuario possa digitar cinco valores numericos e cdastre-os em uma lista,
ja na posicao correta da insercao (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

lista = list()
for n in range(1, 5 + 1):
    valor = int(input('Digite um valor: '))
    if n == 1 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionando ao final da lista...')
    else:
        for i, v in enumerate(lista):
            if valor <= v:
                lista.insert(i, valor)
                print(f'Adicionando na posicao {i} da lista...')
                break

print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
