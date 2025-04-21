dist = float(input('Qual a distância da sua viagem em Km? '))
km1 = dist * 0.50
km2 = dist * 0.45
if dist <= 200:
    print('O valor cobrado para uma viagem de {}Km será de R$ {:.2f} reais.'.format(dist, km1))
else:
    print('O valor cobrado para uma viagem de {}Km será de R$ {:.2f} reais.'.format(dist, km2))