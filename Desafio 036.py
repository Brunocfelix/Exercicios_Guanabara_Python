"""Desafio 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou
então o empréstimo será negado."""
v = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
a = int(input('Quantos anos de financiamento? '))

PM = v / (a * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}' .format(v, a, PM))
if PM > (30 / 100) * s:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
