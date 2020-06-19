n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua media foi {:.1f}!'.format(m))

# Primeira Condicional - Simples
if m >= 6.0:
    print('MEUS PARABENS')

# Segunda Condicional - Composta
if m >= 6.0:
    print('Sua media foi boa! PARABENS!')
else:
    print('Sua media foi ruim! ESTUDE MAIS!')

# Terceira COndicional - Simplificada
print('PARABENS NOVAMENTE!'if m >= 6.0 else 'ESTUDE MAIS, E SEIO')
