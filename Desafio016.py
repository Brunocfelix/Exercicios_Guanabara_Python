#Desafio 016: Crie um programa que leia um número Real qualquer pelo teclado, e mostre na tela a sua porção Inteira;
#	Exemplo: Digite um número 6.127
#			   O número 6.127 tem a parte inteira 6
#Dica: funções dentro da classe math
import math
num = float(input('Digite um número real: '))
print('O número {} tem o número {} como parte inteira!' .format(num, math.trunc(num)))

