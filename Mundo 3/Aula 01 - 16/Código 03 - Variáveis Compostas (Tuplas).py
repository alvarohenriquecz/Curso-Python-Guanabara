# Tuplas aceitam varios tipos de dados, nao necessariamente do mesmo tipo.
pessoa = ('Gustavo', 39, 'M', 99.88) # Tupla "pessoa" com dados str, int, str e float, respectivamente

print(pessoa) # Exibe ('Gustavo', 39, 'M', 99.88)

del(pessoa) # Deleta a tupla "pessoa" inteira 
# del(pessoa[0]) -> Comando impossivel, pois nao se pode deletar um unico elemento tupla
