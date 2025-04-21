from random import randint
from time import sleep
numero = 0
n = 0
computador = randint(1, 10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
while numero != computador:
    numero = int(input('Em que número eu pensei? '))
    if numero != computador:
        n += 1
        print('Ainda não acertou... Tente novamente!')
    else:
        print('BINGO!!, você precisou de {} tentativas para acertar!'.format(n))