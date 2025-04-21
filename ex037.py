n = int(input('Digite um número inteiro: '))
conversao = int(input('Digite qual o número que será a base de conversão? 1- Binário, 2- Octal ou 3- Hexadecimal? '))
binario = bin(n)
octal = oct(n)
hexadecimal = hex(n)
if conversao == 1:
    print('O número inteiro {} é convertido para o número binário {}.'.format(n, binario[2:]))
elif conversao == 2:
    print('O número inteiro {} é convertido para o número octal {}.'.format(n, octal[2:]))
elif conversao == 3:
    print('O número inteiro {} é convertido para o número hexadecimal {}.'.format(n, hexadecimal[2:]))