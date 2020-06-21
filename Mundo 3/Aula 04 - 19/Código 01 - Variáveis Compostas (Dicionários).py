"""
Tuplas: () - Parênteses
Listas: [] - Colchetes
Dicionários: {} - Chaves

Exemplo 1 de Dicionário Vazio:
dados = dict()

Exemplo 2 de Dicionário Vazio:
dados = {}

Exemplo de Dicionário Preenchido com 1 Linha:
dados = {'nome': 'Pedro', 'idade': 25}

Exemplo de Dicionário Preenchido com Múltiplas Linhas:
filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}
"""

dados = {'nome': 'Pedro', 'idade': 25} # Crie um dicionario de "dados" com os indices 'nome' (Pedro) e 'idade' (25)
print(dados['nome']) # Exibe Pedro
print(dados['idade']) # exibe 25

dados['sexo'] = 'M' # Adiciona o indice 'sexo' com o valor 'M' ao final do dicionario "dados"
del dados['idade'] # Deleta o indice 'idade' (com o valor 25) do dicionario "dados"
