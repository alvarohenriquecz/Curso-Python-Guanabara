"""
import <Nome do Modulo> | Iporta tudo contido no modulo
from <Nome do modulo> import <Nome da funcao> | Importa uma funcao especifica do modulo 
from <Nome do Modulo> import <Nome da funcao 1>, <Nome da funcao 2> | Importa duas ou mais funcoes do modulo

Ex:
import math
from math import sqrt
from math import sqrt, ceil

Algumas Funcoes do Modulo math:
ceil - Arredonda o valor para cima
floor - Arredonda o valor para baixo
trunc
pow
sqrt
factorial

Ctrl + Espaco apos digitar "from <Nome do modulo> import" ou somente "import" no Pycharm, lista todas  as funcoes
ou modulos possiveis para importar

Ao tentar importar modulos/bibliotecas que nao estao diretamente integradas ao python , no Pyvharm, ao fazer
isso, uma lampaginha vermelha sera exibida logo ao lado. Clicando sobre ela, e possivel escolher a opcao
para instalar tal Modulo/Biblioteca se ela existir no banco de dados do PypI (Python Package Index).

Para ver quais Modulos/Bibliotecas extras estao instalados, no PyCharm (Windows 10), ir em:
File > Settings... > Project: Nome doProjeto > Project Interpreter
Tambem e possivel adicionar ou remover Modulos/Bibliotecas rapidamente
clicando nos botoes de "+" e de "-", respectivamente

Relação de Módulos/Bibliotecas Integradas Disponíveis: hCódigo 01 - Importações e Módulosttps://docs.python.org/3/library/index.html
Módulos/Bibliotecas Extras: https://pypi.python.org/pypi
"""

from math import sqrt, floor, ceil
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} e igual a {}.'.format(num, raiz))
print('A raiz de {} arredondada para baixo e igual a {}.'.format(num, floor(raiz)))
print('A raiz de {} arredondada para cima e igual a {}.'.format(num, ceil(raiz)))