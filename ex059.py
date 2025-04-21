numero = 0
sair = 5
while numero != sair:
    primeiro = float(input('Primeiro valor: '))
    segundo = float(input('Segundo valor: '))
    numero = int(input('[1] Somar.\n'
                       '[2] Multiplicar.\n'
                       '[3] Maior.\n'
                       '[4] novos números.\n'
                       '[5] Sair do programa.\n'
                       'R: '))
    if numero == 1:
        soma = primeiro + segundo
        print('Você selecionou a soma entre {} e {}, que é {}.'.format(primeiro, segundo, soma))
    elif numero == 2:
        multi = primeiro * segundo
        print('Você selecionou a multiplicação entre {} e {}, que é {}.'.format(primeiro, segundo, multi))
    elif numero == 3:
        maior = max(primeiro, segundo)
        print('Você selecionou o maior número entre {} e {}, que é {}.'.format(primeiro, segundo, maior))
    elif numero == 4:
        print('Retornando ao menu principal...')
    elif numero == 5:
        print('Finalizando...')