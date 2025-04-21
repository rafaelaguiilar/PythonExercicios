from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}!'.format(computador, jogador))

#n = int(input('Olá, eu sou o computador, duvido você acertar o número de 0 a 5 que eu estou pensando agora! Digita ai: '))
#if n == 4:
#    print('UALLLLLLL, Você é um bruxo cibernético ? você acertou exatamente o número {} que estava programado... Digo, que eu estava pensando!'.format(n))
#else:
#    print('Nahhh, você errou feio! eu pensei no número {}, Mais sorte na proxima!'.format(4))