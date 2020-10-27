"""Desafio 068: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo"""
from random import randint
v = 0
print('=-=' * 10)
print('Vamos JOGAR PAR OU ÍMPAR!')
print('=-=' * 10)

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper()[0].strip()
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}.\nTotal de {total} ', end='')
    print('Deu PAR!' if total % 2 == 0 else 'Deu ÍMPAR')
    print('-' * 30)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('=-=' * 13)
print(f'GAME OVER! Você Venceu {v} vezes')