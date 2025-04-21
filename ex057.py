sexo = ' '
while sexo not in 'MF':
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Valores incorretos, tente novamente.')
    else:
        print('Sexo {} registrado com sucesso.'.format(sexo))