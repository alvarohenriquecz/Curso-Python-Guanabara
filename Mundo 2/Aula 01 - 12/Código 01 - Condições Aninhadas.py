"""
Exemplo de Estrutura Condicional Aninhada:
if <CONDICAO 1>:
    <COMANDOS A>
elif <CONDICAO 2>:
    <COMANDOS B>
elif <CONDICAO 3>:
    <COMANDOS C>
else:
    <COMANDOS D>

Nota 1: E possivel utilizar quantos "elif" forem necessarios.

Nota 2: Nunca e possivel utilizar "elif" sem "if", porem o "else" e sempre opcional
"""
nome = str(input('Qual e o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome e bem popular no Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome e bem normal')
print('Tenha um bom dia, {}!'.format(nome))

