"""
NOME:
Estrutura de Repeticao com variavel de controle

Exemplos didiaticos:
laco c no intervalo(1, 10):
    passo
pega

laco c no intervalo(0, 3):
    se moeda:
        pega
    passo
    pula
passo
pega

Exemplos reais:
for c in range(1, 10)
    passo
pega

for c in range(0, 3):
    if moeda:
        pega
    passo
    pula
passo
pega
"""
#Exemplo 1 - Imprime 'oi' 6 vezes
for c in range(0, 6):
    print('oi')
print('fim 1')

# exemplo 2 - imprime todos os numeros de 1 a 6 (7 - 1), em ordem crescente
for c in range(1, 7):
    print(c)
print('fim 2')

# exemplo 3 - imprime todos os numeros de 6 a 1, em ordem decrescente
for c in range(6, 0, -1):
    print(c)
print('fim 3')

# exemplo 4 - imprime todos os numeros de 0 a 6, em ordem crescente, pulando de 2 em 2
for c in range(0, 7, 2):
    print(c)
print('fim 4')

# exemplo 5 - imprime todos os numeros de 0 a 'n' (entrada do usuario)
n = int(input('Digite um numero: '))
for c in range(0, n + 1):
    print(c)
print('fim 5')

# exemplo 6 - imprime todos os numeros de 'i' a 'f', pulando 'p' passos a cada iteracao (entradas do usuario)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print('fim 6')

# exemplo 7 - Pede para o usuario inserir um valor diferente 4 vezes e soma todos num resultado final
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatorio de todos os valores foi {}.'.format(s))
print('fim 7')
