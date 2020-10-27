"""Desafio 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar;
Se é a hora de ele se alistar;
Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou o tempo que passou do prazo."""
from datetime import date
ano = int(input('Digite o ano de nascimento: '))
ano2 = date.today().year
idade = ano2 - ano
print('Quem nasceu em {} tem {} anos em {}.' .format(ano, idade, ano2))

if idade < 18:
    saldo = 18 - idade
    print('Ainda falta(m) {} ano(s) para o alistamento.' .format(saldo))
    anofuturo = ano2 + saldo
    print('Seu alistamento será em {}' .format(anofuturo))

elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} ano(s).' .format(saldo))
    anopassado = ano2 - saldo
    print('Seu alistamento foi em {}.' .format(anopassado))


else:
    print('Você tem que ir se alistar IMEDIATAMENTE!')