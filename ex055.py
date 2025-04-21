maior_peso = 0
menor_peso = 0

for c in range(0, 6):
    peso = float(input('Peso da {}º pessoa: '.format(c + 1)))
    if c == 0:  # Para a primeira entrada, inicializamos maior e menor peso
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'O maior peso digitado foi {maior_peso:.2f} kg')
print(f'O menor peso digitado foi {menor_peso:.2f} kg')
