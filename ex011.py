n1 = float(input('Quantos metros de largura a parede tem: '))
n2 = float(input('Quantos metros de altura a parede tem: '))
ar = n1 * n2
lit = ar / 2
print('A área total a ser pintada é de {:.2f}m² e precisa de {:.2f}l de tinta para pintar ela completamente.'.format(ar, lit))