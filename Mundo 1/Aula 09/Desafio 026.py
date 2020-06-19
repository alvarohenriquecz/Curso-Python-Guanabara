"""
Desafio 026: Primeira e Ultima Ocorrencia de uma String

Faca um programa que leia uma frase pelo teclado e mostre: 

> Quantas vezes aparece a letra "A".
> Em que posicao ela aparece a primeira vez.
> Em que posiao ela aparece a ultima vez.
"""
frase = input('Digite uma frase: ').upper().strip()
qtd = frase.count('A')
pos1 = frase.find('A')+1
pos2 = frase.rfind('A')+1

print('\nA sua frase tem {} letra(s) "A".'.format(qtd), end='\n')
print('A primeira aparece na posicao numero {} \n e a ultima aparece na posiao numero {}!'.format(pos1, pos2))
