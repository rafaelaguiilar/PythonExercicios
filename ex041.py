from datetime import date
ano = int(input('Digite o ano de nascimento: '))
if date.today().year - ano <= 9:
    print('Você tem {} anos, sua categoria é \033[34mMIRIM!\033[m'.format(date.today().year - ano))
elif date.today().year - ano <= 14:
    print('Você tem {} anos, sua categoria é \033[34mINFANTIL!\033[m'.format(date.today().year - ano))
elif date.today().year - ano <= 19:
    print('Você tem {} anos, sua categoria é \033[34mJUNIOR!\033[m'.format(date.today().year - ano))
elif date.today().year - ano <= 20:
    print('Você tem {} anos, sua categoria é \033[34mSÊNIOR!\033[m'.format(date.today().year - ano))
elif date.today().year - ano > 20:
    print('Você tem {} anos, sua categoria é \033[34mMASTER!\033[m'.format(date.today().year - ano))