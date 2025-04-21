import random
from random import randint

jokenpo = str(input('Faça sua escolha.\n'
                    'PEDRA\n'
                    'PAPEL\n'
                    'TESOURA\n')).upper()
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.choice(lista)
if jokenpo == 'PEDRA' and computador == 'TESOURA':
    print('Parabéns, você ganhou... Eu escolhi {}!'.format(computador))
elif jokenpo == 'PAPEL' and computador == 'PEDRA':
    print('Parabéns, você ganhou... Eu escolhi {}!'.format(computador))
elif jokenpo == 'TESOURA' and computador == 'PAPEL':
    print('Parabéns, você ganhou... Eu escolhi {}!'.format(computador))
elif jokenpo == computador:
    print('Empatamos, tente novamente!')
else:
    print('Eu ganhei! Eu escolhi {}!'.format(computador))