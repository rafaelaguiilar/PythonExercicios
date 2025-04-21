r1 = float(input('Informe o comprimento da reta 1: '))
r2 = float(input('Informe o comprimento da reta 2: '))
r3 = float(input('Informe o comprimento da reta 3: '))
soma1 = r1 + r2
soma2 = r1 + r3
soma3 = r2 + r3
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[34mNestas condições descritas, as retas formarão um triângulo! ', end='')
    if r1 == r2 == r3:
        print('\033[31mEquilátero!')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('\033[33mIsósceles!')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('\033[32mEscaleno!')
else:
    print('\033[31mNestas condições descritas, as retas NÃO formarão um triângulo!')