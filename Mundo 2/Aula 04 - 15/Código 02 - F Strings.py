"""
NOTA: 
A partir da versao 3.6, o Python incluiu uma PEP onde passou a suportar strings, que ajudam a
simplificar a formatacao de variaveis no meio de prints e textos dentro de outras variaveis.

Exemplos: 

Primeiro Metodo - Python 2 - %:
num = 10
print('Dez é igual a %d.' % (num))

Metodo Anterior - Python 3 - format:
num = 10
print('Dez e igual a {}.'.format(num))

Metodo Novo - Python 3.6+ - F string:
num = 10
print(f'Dez e igual a {num}.')
"""
num = 10
print('Primeiro Método - Python 2 - %:')
print('Dez é igual a %d.' % num)
print('')
print('Método Anterior - Python 3 - Format:')
print('Dez é igual a {}.'.format(num))
print('')
print('Método Novo - Python 3.6+ - F String:')
print(f'Dez é igual a {num}.')
