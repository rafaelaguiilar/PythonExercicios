from datetime import date
from operator import neg

ano = int(input('Qual seu ano de nascimento? '))
if date.today().year - ano < 18:
    print('Ainda você vai se alistar ao serviço militar, falta apenas {} anos.'.format(neg(date.today().year - ano - 18)))
elif date.today().year - ano == 18:
    print('Chegou a hora de se alistar, você ja tem {} anos.'.format(date.today().year - ano))
elif date.today().year - ano > 18:
    print('Passou do tempo de alistamento em {} anos.'.format(date.today().year - ano - 18))