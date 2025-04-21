n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro valor é \033[1;34mMAIOR\033[m!')
elif n2 > n1:
    print('O segundo valor é \033[1;32mMAIOR\033[m!')
elif n1 == n2:
    print('Não existe valor maior, os dois são \033[1;33miguais\033[m!')