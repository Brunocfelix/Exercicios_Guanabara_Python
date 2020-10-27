# Desafio 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto;
from datetime import date
ano = int(input('Qual ano você quer analisar? Digite 0 se quiser analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BiSSEXTO!' .format(ano))
else:
    print('O ano {} não é BISSEXTO!' .format(ano))
