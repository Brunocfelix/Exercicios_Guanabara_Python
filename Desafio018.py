# Desafio 018: Faça um programa que leia um ângulo qualquer, e mostre na tela o valor do seno, cosseno e
# tangente desse ângulo;
#import math
#ang = float(input('Digite um ângulo qualquer: '))
#seno = math.sin(math.radians(ang))
#print('O ângulo de {} tem o Seno de {:.2f}' .format(ang, seno))
#cosseno = math.cos(math.radians(ang))
#print('O ângulo de {} tem o Cosseno de {:.2f}' .format(ang, cosseno))
#tangente = math.tan(math.radians(ang))
#print(' O ângulo de {} tem a Tangente de {:.2f}' .format(ang, tangente))

from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(ang))
print('O ângulo de {} tem o Seno de {:.2f}' .format(ang, seno))
cos = cos(radians(ang))
print('O ângulo de {} tem o Cosseno de {:.2f}' .format(ang, cos))
tan = tan(radians(ang))
print('O ângulo de {} tem a tangente de {:.2f}' .format(ang, tan))