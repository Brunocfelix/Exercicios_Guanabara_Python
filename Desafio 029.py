"""Desafio 029: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado, se não ultrapassar, não precisa mostrar nada
A multa vai custar R$7,00 por cada Km acima do limite;"""
velocidade = float(input('Digite a velocidade do carro naquele instante: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Sua velocidade era de {} km/h e estava acima do limite de 80km/h'.format(velocidade))
    print('Você foi multado e deverá pagar um valor de R${:.2f}' .format(multa))
else:
    print('Sua velocidade era de {} km/h e estava dentro do limite de 80km/h'.format(velocidade))
