"""Desafio 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
será formado:
Equilátero: todos os lados iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes"""
# Desafio 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo.
print('-*=*-' * 20)
print('\033[34mAnalisador de Triângulos\033[m')
print('-*=*-' * 20)
p1 = float(input('Primeiro Segmento: '))
p2 = float(input('Segundo Segmento: '))
p3 = float(input('Terceiro Segmento: '))
if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print('Os segmentos acima PODEM formar um Triângulo', end=' ')
    if p1 == p2 == p3:
        print('EQUILÁTERO!')
    elif p1 != p2 != p3 != p1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM formar um Triângulo.')
