# Desafio 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2;
L = float(input('Digita a Largura da parede, em metros: '))
A = float(input('Digite a Altura da parede, em metros: '))
S = L * A
s1 = S / 2
print('Sua parede tem a dimensão de: {:.2f} x {:.2f}, e sua área é de: {:.2f}m²' .format(L, A, S))
print('Para pintar essa parede, a quantidade de tinta necessária será de: {:.2}l' .format(s1))
