"""
Desafio 062: Super Progressao Aritmetica v3.0

Melhore o Desafio 061, perguntando para o usuario se ele quer mostrar mais 
algum termo. O programa encerra quando ele disser que quer mostrar 0 termos.
"""

primero = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primero + (10 - 1) * razao
print('\n10 Primeiros Termos da PA com razao {} (Iniciando em {}): '.format(razao,primero))
print(primero, end=' - ')

while primero < decimo:
    primero += razao
    if decimo == decimo:
        print(primero, end='')
    else:
        print(primero, end=' - ')

print('\n')
escolha = int(input('Quer ver mais quantos termos? Digite 0 para nao ver mais nenhum: '))
atual = primero

while escolha != 0:
    ultimo = atual + (escolha - 1) * razao 
    print('{}'.format(atual), end=' - ')
    while atual < ultimo + razao:
        atual += razao
        if atual > ultimo:
            print(atual, end='')
        else:
            print(atual, end=' - ')
    print('\n')
    escolha = int(input('Quer ver mais quantos termos? Digite 0 para nao ver mais nenhum: '))

print('\nPrograma finalizando!')
