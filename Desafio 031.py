"""Desafio 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas;"""
dist = float(input('Qual é a distância da viagem? '))
p1 = dist * 0.50
p2 = dist * 0.45
if dist <= 200:
    print('A distância é de {:.2f}Km, portanto, o valor da passagem é de R${:.2f}'.format(dist, p1))
else:
    print('A distância é de {:.2f}Km, portanto, o valor da passagem é de R${:.2f}'.format(dist, p2))
