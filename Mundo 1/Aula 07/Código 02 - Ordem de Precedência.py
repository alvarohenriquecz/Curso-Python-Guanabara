"""
Ordem de Precedencia (O que é levado em conta primeiro código do python) :
# 1 () - Parenteses
# 2 ** - Potência
# 3 *, /, // e % - Multiplicação, Divisão, Divisão inteira e Resto da divisão
# 4 + e - Adição ou subtração
"""
print(5 + 3 * 2) # Primeiro a multiplicação e depois a adição
print( 3 * 5 + 4 ** 2) # Primeiro se resolve a Exponenciação, depois a Multiplicação, e por fim a adição
print(3 * ( 5 + 4) ** 2) # Primeiro parenteses, depois a exponenciação e depois a multiplicação
