import random
n1 = input('Nome primeiro aluno: ')
n2 = input('Nome segundo aluno: ')
n3 = input('Nome terceiro aluno: ')
n4 = input('Nome quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno(a) escolhido(a) é {}'.format(escolhido))