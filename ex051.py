primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
n = int(input('Quantos elementos exibir: '))

ultimo = primeiro + (n - 1) * razao
ultimo = ultimo + 1
for c in range(primeiro, ultimo, razao):
    print(c, end=' -> ')
print('ACABOU')