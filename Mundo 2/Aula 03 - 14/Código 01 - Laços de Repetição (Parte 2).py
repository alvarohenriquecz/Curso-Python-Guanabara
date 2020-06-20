"""
Nome:
Estrutura de Repeticao com teste Logico

Nota:
Usar o for quando o laco tiver um numero predefinido de repeticoes. caso contrario, usar o while.

Exemplos didaticos:
enquanto nao chegar na maca:
    passo
pega

enquanto nao chegaar na maca:
    se tem chao:
        passo
    se tem buraco:
        pula
    se tem moeda:
        pega
pega

exemplos reais:
while not chegar_na_maca:
    passo
pega

while not chegar_na_maca:
    if tem_chao:
        passo
    if tem_buraco:
        pula
    if tem_moeda:
        pega
pega
"""

# Exemplo 1.1 - Imprime todos os numeros de 1 a 10, em ordem crescente, usando o laco for
for c in range(1, 11):
    print(c)
print('FIM 1.1')

# Exemplo 1.2 - Faz o mesmo que o exemplo 1.1, porem usando o comando while 
c = 1
while c < 11:
    print(c)
    c += 1
print('FIM 1.2')

# Exemplo 2 - Pede para o usuario inserir um valor N vezes (indefinido), so parando quando 0 for digitado
n = 1
while n != 0:   # flag/condicao de parada
    n = int(input('Digite um valor: '))
print('FIM 2')

# Exemplo 3 - Pede para o usuario inserir um valor N vezes 
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N]? ')).upper()
print('FIM 3')

# Exemplo 4 - pede para o usuario inserir N valores (indefinido) e diz quantos destes sao pares e quantos sao impares
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('Voce digitou {} Numeros pares e {} numeros impares!'.format(par, impar))
print('FIM 4')
