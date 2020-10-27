#DESAFIO 004: Faça um programa que leia algo (qualquer coisa, misturado ou não)
#pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis entre ele.
#	• Irá utilizar várias opções de "is", dentro de um mesmo exercício.
a = input('Digite Algo: ')
print('O tipo primitivo desse valor é:', type(a))
print('Este valor só tem espaços?', a.isspace())
print('Este valor é alfabético?', a.isalpha())
print('Este valor está maiúsculo?', a.isupper())
print('Este valor é um número?', a.isnumeric())
print('É alfa-númerico?', a.isalnum())
print('Está em minúsculo?', a.islower())
