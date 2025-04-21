soma_idades = 0
maior_idade_homem = 0
nome_velho = ''
count_mulheres = 0
for c in range(1, 5):
    print('----- {}º PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idades += idade
    if c == 0 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    else:
        if sexo in 'Mm' and idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        count_mulheres += 1
media = soma_idades / 4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(count_mulheres))
