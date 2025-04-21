sal = float(input('\033[1;30;43mInforme o seu salário: \033[m'))
if sal >= 1250:
    ali: float = (sal * 10 / 100) + sal
else:
    ali: float = (sal * 15 / 100) + sal
print('Quem ganhava \033[1;31mR${:.2f}\033[m passa a ganhar \033[1;34mR${:.2f}\033[m reais agora.'.format(sal, ali))