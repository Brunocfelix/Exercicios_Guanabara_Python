"""Desafio 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e a condição de pagamento:
À vista dinheiro/cheque: 10% de desconto
À vista no cartão: 5% de desconto
Em até 2x no cartão: preço normal
Em 3x ou mais no cartão: 20% de Juros"""
print('{:=^40}'.format(' \033[1:30:41mLOJAS BRUNO\033[m '))
valor = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
forma = int(input('Qual é a opção da forma de pagamento? '))

if forma == 1:
    total = valor - (10 / 100) * valor
elif forma == 2:
    total = valor - (5 / 100) * valor
elif forma == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros'.format(parcela))
elif forma == 4:
    total = valor + (20 / 100) * valor
    parcelas = int(input('Quantas parcelas? '))
    parcela = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, parcela))
print('Sua compra de R${:.2f} irá custar um valor de R${:.2f} no final.'.format(valor, total))
