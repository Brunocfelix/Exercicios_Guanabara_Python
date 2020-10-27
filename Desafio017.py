# Desafio 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo. Calcule e mostre o comprimento da hipotenusa;
import math
co = float(input('Digite a medida do cateto oposto ao ângulo: '))
ca = float(input('Digite a medida do cateto adjacente ao ângulo: '))
print('A Hipotenusa do triângulo retângulo vale: {:.2f}' .format(math.hypot(co, ca)))

