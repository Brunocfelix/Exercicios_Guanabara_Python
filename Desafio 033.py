# Desafio 033: Faça um programa que leia três números e mostre qual é o número maior, e qual é o número menor;
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor número digitado foi: {}' .format(menor))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número digitado foi: {}' .format(maior))
