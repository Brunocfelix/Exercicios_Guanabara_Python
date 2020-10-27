# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude a ele, lendo o nome dos quatro alunos, e escrevendo o nome do escolhido;
#Desafio 020: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada;
import random
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)



