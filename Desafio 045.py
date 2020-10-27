# Desafio 045: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('Suas opções são:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogada = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
print('-*-' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogada]))
print('-*-' * 10)

if jogada == 0 and computador == 2:
    print('JOGADOR VENCE!')
elif jogada == 0 and computador == 1:
    print('COMPUTADOR VENCE!')
elif jogada == 1 and computador == 0:
    print('JOGADOR VENCE!')
elif jogada == 1 and computador == 2:
    print('COMPUTADOR VENCE!')
elif jogada == 2 and computador == 0:
    print('COMPUTADOR VENCE!')
elif jogada == 2 and computador == 1:
    print('JOGADOR VENCE!')
elif jogada == computador:
    print('JOGO EMPATADO')
else:
    print('Jogada Inválida!')