'''a = float(input('Quanto mede o cateto oposto? '))
b = float(input('Quanto mede o cateto adjacente? '))
raiz = (a ** 2 + b ** 2) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(raiz))'''

from math import hypot
a = float(input('Quanto mede o cateto oposto? '))
b = float(input('Quanto mede o cateto adjacente? '))
raiz = hypot(a, b)
print('O valor da hipotenusa é {:.2f}'.format(raiz))