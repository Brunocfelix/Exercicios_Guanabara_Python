# Desafio 030: Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou IMPAR;
num = int(input('Digite um número inteiro: '))
if (num % 2 == 0):
    print('O número {} é PAR' .format(num))
else:
    print('O número {} é IMPAR' .format(num))

