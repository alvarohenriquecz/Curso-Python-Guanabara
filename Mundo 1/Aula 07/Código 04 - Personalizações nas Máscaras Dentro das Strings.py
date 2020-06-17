# Personalizações nas Máscaras Dentro das Strings

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome)) # Exibe normalmente o valor inserido
print('Prazer em te conhecer, {:20}!'.format(nome)) # Exibe o valor inserido com 20 caracteres apenas
print('Prazer em te conhecer, {:>20}!'.format(nome)) # Exibe o valor inserido com 20 caracteres e alinhado a direita
print('Prazer em te conhecer, {:<20}!'.format(nome)) # Exibe o valor inserido com 20 caracteres e alinhado a esquerda
print('Prazer em te conhecer, {:^20!}'.format(nome)) # Exibe o valor inserido com 20 caracteres e alinhado no centro
print('Prazer em te conhecer, {:*^20}'.format(nome))
""" Exibe o valor inserido com 20 caracteres, alinhado no centro
e com o sinal de "*" preenchendo os espaços vazios """
