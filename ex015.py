dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
c = dias * 60 + km * 0.15
print('O Total a pagar é de R$ {:.2f}'.format(c))
