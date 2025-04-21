valor = float(input('Digite o valor do produto: R$'))
condicao = int(input('Digite 1 - Para à vista (dinheiro/cheque) 10% de desconto\n'
                     'Digite 2 - Para à vista no cartão 5% de desconto\n'
                     'Digite 3 - Para 2x no cartão sem juros\n'
                     'Digite 4 - Para 3x ou mais no cartão e 20% de juros\n'))
if condicao == 1:
    valor = valor - (valor * 10 / 100)
    print('À vista (dinheiro/cheque) 10% de desconto fica por R${:.2f}'.format(valor))
elif condicao == 2:
    valor = valor - (valor * 5 / 100)
    print('À vista no cartão 5% de desconto fica por R${:.2f}'.format(valor))
elif condicao == 3:
    valor = valor / 2
    print('2x no cartão sem juros fica por R${:.2f} mês.'.format(valor))
elif condicao == 4:
    valor = valor + (valor * 20 / 100)
    parcelas = valor / 3
    print('3x ou mais no cartão e 20% de juros fica R${:.2f} mês. Total de R${:.2f}'.format(parcelas, valor))