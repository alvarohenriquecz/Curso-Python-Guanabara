# Personalidades na Sintaxe do Print
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 / n2 
m = n1  * n2
d  = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma e {}, o produto e {} e a divisao e {} '.format(s, m, d)) # Exibe os resultados de soma, produto e divisão
print('A soma e {}, o produto e {} e a divisao e {:.3f}'.format(s, m, d))
""" Exibe o resultado da divisão com 3 casas decimais """
print('A soma e {}, o produto e {} e a divisao e {}'.format(s, m, d), end = ' ')
""" Exibe o resultado sem quebrar a linha, dando um espaço ao invés disso"""
print('A soma e {}, o produto e {} e a divisao e {}'.format(s, m, d), end=' >>> ')
""" Exibe o resultado sem quebrar a linha, dando um  ">>>" ao inves disso """
print('A soma e {}, \no produto e {} \ne a divisao e {}'.format(s, m, d))
""" Exibe o resultado com duas quebras de linha no meio do print """
print('Divisão inteira {} e potencia {}'.format(di, e))