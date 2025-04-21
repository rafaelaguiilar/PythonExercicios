v = float(input('Velocidade do veículo foi de: '))
m = (v - 80) * 7
if v > 80:
    print('Você ultrapassou o limite de velocidade de 80Km/h, você foi multado em R${:.2f} reais.'.format(m))
else:
    print('Velocidade inferior ou igual a 80Km/h, Sem multas!')