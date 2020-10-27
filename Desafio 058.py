'''Desafio 058: Melhore o jogo do DESAFIO 028, onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora, o jogador irá tentar adivinhar até acertar, mostrando no final quantos palpites
forem necessários para vencer.'''
"""Desafio 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu;"""
from random import randint
from time import sleep

cont = 1
computador = randint(0, 10)
print('-*-' * 20)
print('\033[1;7;30mEstou pensando em um número de 0 a 10...\033[m')
sleep(2)
print('Será que você consegue adivinhar qual foi?')
jogador = int(input('Qual é o seu palpite? '))

while jogador != computador:
    if jogador < computador:
        print('Mais... tente mais uma vez')

    elif jogador > computador:
        print('Menos... tente mais uma vez')
    jogador = int(input('Qual é o seu palpite? '))
    cont += 1
print('Parabéns, você conseguiu me vencer!')
print('Acertou com {} tentativas'.format(cont))