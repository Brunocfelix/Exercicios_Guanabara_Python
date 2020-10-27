# Desafio 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares
# ela pode comprar.
# Considere US$1,00 = R$3,27
real = float(input('Digite o valor em Reais que você tem na carteira: R$'))
dolar = real / 3.27
print('Com R${:.2f}, você poderá comprar: US${:.2f}!' .format(real, dolar))



