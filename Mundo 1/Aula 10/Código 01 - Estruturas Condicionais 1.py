"""
Nota 1: Todo metodo "()" (abre e fecha parenteses) no final.
Por exemplo, em "arro.siga()", "carro" e o objeto e "siga()" e o metodo

Nota 2: Todos os exercicios e desafios feitos ate o momente utilizam Estruturas Sequenciais.
A partit de agora, serao apresentadas as Estruturas Condicionais.

Nota 3: O espacamento lateral antes dos comandos de uma Estrutura Condicional e chamado Identacao
Uma identacao pode ser criada pressionando a tecla "tab".

Nota 4: Em uma Estrutura Condicional simples de "se" e "senao", o bloco do comando do "se" e 
executado se a condicao for verdadeira (True), enquanto o bloco de comandos do "senao" e
executado se a condicao for falsa (False).

Exemplo de Condicional Simples:
if <CONDICAO>:
    <COMANDOS A>
else:
    <COMANDOS B>

Exemplo de Condicional simplificada:
print('Frase a exibir se a condicao se cumprir' if <CONDICAO> else 'Frase a exibir se a condicao nao se umprir')
"""
temp = int(input('Quantos anos tem seu carro? ')) # Atribui a variavel "tempo" o valor de um numero inteiro
if tempo <= 3:  # Se a variavel "tempo" receber um valor igual ou menor do que 3...
    print('Carro novo!') # Exibe "Carro novo"
else :
    print('Carro velho!')   # Exibe "arro velho!"
print('---FIM---') # Exibe "---FIM---" independete do Metodo do resultado e da condicao acima
