"""Desafio 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão, usando a estrutura while."""

"""Desafio 051: Desenvolva um programa que leia o primeiro termo, e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""

print('Gerador de PA')
print('=-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> ' .format(termo), end='')
    termo += razao
    cont += 1
print('FIM')