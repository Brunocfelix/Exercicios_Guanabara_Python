# Desafio 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto;
p = float(input('Digite o preço do produto:R$'))
p1 = p * 0.95
print('O produto que custava R${:.2f}, na promoção, com desconto de 5%, irá sair no valor de:R${:.2f}'.format(p, p1))

