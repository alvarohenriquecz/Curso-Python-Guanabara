filme = {'titulo' : 'Star Wars',
        'ano' : 1977,
        'diretor' : 'George Lucas'} # Cria um dicionario "filme" com 3 chaves (keys) e 3 valores (values)

print(filme.keys()) # exibe as chaves do dicionario "filme"
print(filme.values()) # exibe os valores do dicionario "filme"
print(filme.items()) # exibe os itens (chave + valor) do dicionario "filme"

for k, v in filme.items(): # Para cada chave (k) e o valor (v) nos itens do dicionario "filme"...
    print(f'O {k} e {v}') # Exibe formatado a chave (k) atual  o seu respectivo valor (v)
    