# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por
# um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
D = int(input('Por quantos dias o carro ficou alugado?'))
Km = float(input('Quantos km o carro rodou? '))
Valor = (D * 60) + (Km * 0.15)
print('O valor total a pagar é de R${:.2f}' .format(Valor))

