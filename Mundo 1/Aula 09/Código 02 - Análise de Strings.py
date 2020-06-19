"""
[C] [u] [r] [s] [o] [ ] [e] [m] [ ] [V] [í ] [d ] [e ] [o ] [  ] [P ] [y ] [t ] [h ] [o ] [n ]
[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18] [19] [20]
"""

frase = 'Curso em video Python'

print(len(frase)) # Exibe a quantidade de caracteres de uma string (no caso, 21)
print(frase.count('o'))
"""Exibe a quantidade de vezes que o caractere entre parenteses (no caso, "o" minusculo)
aparece na string (no caso, 3) """
print(frase.count('o', 0, 13))
""" Idem ao caso acima, porem aqui foi incluido um fatiamento do indice [0] ao [13]-1, exibindo "1" """

print(frase.count('o', 0, 14)) # Idem ao caso acima, porem aqui o indice final ficou  sendo [14]-1, exibindo "2"
print(frase.find('deo')) #Exibe o indice inicial (11, no caso) do que esta entre parenteses
print(frase.find('Android')) # QUando se procura na string algo que nao esta presente, o valor exibido e "-1"
print('Curso' in frase) # Verifica se o que esta ntre aspas esta presente na string, e se sim, exibe "True"
