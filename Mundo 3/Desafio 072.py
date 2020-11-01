"""Desafio 072: Crie um programa que tenha uma tupla totalmente preenchida com
uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso."""

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    digiteum = int(input('Digite um número entre 0 e 20: '))
    if 0 <= digiteum <= 20:
        break
    print('Tente novamente... ', end='')
print(f'Você digitou o número {numeros[digiteum]}.')


