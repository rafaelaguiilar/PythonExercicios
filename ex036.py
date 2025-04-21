casa = int(input('Qual o valor R$ da casa? '))
salario = int(input('Qual é o salário do comprador? '))
ano = int(input('Em quantos anos pretende pagar? '))
if salario * 0.3 > casa / (ano * 12):
    print('\033[4;34mParabéns, o banco aprovou o seu emprestimo. Sua parcela será de R$ {:.2f} por {} meses!\033[m'.format(casa / (ano * 12), ano * 12))
elif salario * 0.3 < casa / (ano * 12):
    print('\033[4;31mInfelizmente sua renda não alcançou o limite estabelecido, o emprestimo não será efetivado.\033[m')