"""Desafio 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para Salários superiores a R$1250,00, calcule um aumento de 10%.
Para salários inferiores ou iguais, o aumento é de 15%;"""
sal = float(input('Digite o salário atual do funcionário: '))
if sal > 1250:
    salnovo = sal + (10/100)*sal
    input('O salário teve um aumento de 10%, logo, o funcionário passará a receber R${:.2f}'.format(salnovo))
else:
    salnovo = sal + (15/100)*sal
    input('O salário teve um aumento de 15%, logo, o funcionário passará a receber R${:.2f}'.format(salnovo))
