"""Desafio 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seus status, de acordo com a tabela abaixo:
Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso ideal
De 25 até 30: Sobrepeso
De 30 até 40: Obesidade
Acima de 40: Obesidade Mórbida"""
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))

IMC = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(IMC))

if IMC < 18.5:
    print('Você está abaixo do peso ideal!')
elif 18.5 <= IMC < 25:
    print('PARABÉNS! Você está na faixa de Peso Ideal!')
elif 25 <= IMC < 30:
    print('Você está em Sobrepeso, cuidado!')
elif 30 <= IMC < 40:
    print('Você está em Obesidade!')
else:
    print('Você está em Obesidade Mórbida, cuidado!')
