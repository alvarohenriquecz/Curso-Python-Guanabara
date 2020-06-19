"""
[C] [u] [r] [s] [o] [ ] [e] [m] [ ] [V] [í ] [d ] [e ] [o ] [  ] [P ] [y ] [t ] [h ] [o ] [n ]
[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18] [19] [20]

[ ] [ ] [ ] [A] [p] [r] [e] [n] [d] [a] [  ] [P ] [y ] [t ] [h ] [o ] [n ] [  ] [  ]
[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18]
"""

frase = 'Curso em video Python'
frase2 = '      Aprenda Python      '
print(frase.replace('Python','Android')) # Exibe a string com um termo existente substituindo por outro
print(frase.upper()) # Exibe a string toda em letras maiusculas
print(frase.lower()) # Exibe a string toda em letras minusculas
print(frase.capitalize()) # Exibe a string capitalixada (com apenas o primeiro caractere da frase em letra maiuscula)
print(frase.title()) # Exibe a string estilo titulo (com o primeiro caractere de cada  palavra maiuscula)
print(frase.title()) # Exibe a string estilo titulo (com o primeiro caractere de cada palacra em letra maiuscula)
print(frase) # A string original nao foi alterada permanentemente por nenhum dos comandos utilizzados acima

print('') # Linha em branco para separar os comandos direcionados a cada string

print(frase2.strip()) # Remove todos os espacos excedentes a string
print(frase2.rstrip()) # Remove os espacos excedentes apenas do lado direito da string (inclusao do "r" no comando)
print(frase2.lstrip()) # Remove os espacos excedentes apenas do lado esquerdo da string (inclusao do "l" no comando)
print(frase2) # Novamente, a string original nao foi alterada permanentemente por nenhum dos comandos utilizados acima

print('') # Linha em branco

frase = fras.replace('Python', 'Android') # Desta forma sim, a string original é substituida permanentemente
print(frase) # Exibe a string original ja com as modificacoes feitas acima

