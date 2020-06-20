nome = 'jose'
idade = 33
salario = 987.3
print(f'0 {nome} tem {idade} anos e ganha R$ {salario:.2f}.') # Salario com 2 casas decimais
print(f'O {nome:^20} tem {idade} anos.') # Nome centralizado e ocupando 20 caracteres
print(f'{nome:-^20}') # Nome centralizado e ocupando 20 caracteres com "-" no lugar dos espacos
print(f'{nome:->20}') # Nome alinhado a direita e ocupando 20 caracteres com "-" no lugar dos espacos
print(f'{nome:-<20}') # Nome alinhado a esquerda e ocupando 20 caracteres com "-" no lugar dos espacos
