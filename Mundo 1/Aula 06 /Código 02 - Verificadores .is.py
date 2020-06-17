n = input('Digite algo: ')
print(n.isnumeric()) # Verifica se o que foi digitado é ou pode se tornar um valor numerico, retorna true se sim
print(n.isalpha()) # Verifica se o que foi digitado é uma letra ou contem apenas letras, retorna true se sim
print(n.isalnum()) # Verifica se o que foi digitado contém apenas letras e numeros, retorna  true se sim
print(n.isupper()) # Verifica se o que foi digitado contém apenas aiusculas, retorna true se sim
# Existem ainda outros metodos "is", como "islower()", "isspace()" etc.
