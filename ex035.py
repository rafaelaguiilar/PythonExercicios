r1 = float(input('Informe o comprimento da reta 1: '))
r2 = float(input('Informe o comprimento da reta 2: '))
r3 = float(input('Informe o comprimento da reta 3: '))
soma1 = r1 + r2
soma2 = r1 + r3
soma3 = r2 + r3
if soma1 > r3 and soma2 > r2 and soma3 > r1:
    print('\033[34mNestas condições descritas, as retas formarão um triângulo!')
else:
    print('\033[31mNestas condições descritas, as retas NÃO formarão um triângulo!')