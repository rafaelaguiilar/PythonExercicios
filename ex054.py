from datetime import date
from itertools import count

menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    if date.today().year - ano < 21:
        menor += 1
    else:
        maior += 1
print('\nAo todo tivemos {} pessoas maiores de idade\n'
      'E também tivemos {} pessoas menores de idade'.format(maior, menor))


