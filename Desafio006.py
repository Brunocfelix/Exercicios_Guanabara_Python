# Desafio 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada;
n = int(input('Digite um número: '))
n1 = n*2
n2 = n*3
n3 = n**(1/2)

print('O número digitado foi: {} \nO seu dobro é: {}'.format(n, n1))
print('O seu triplo é: {} \nA sua raiz quadrada vale: {}' .format(n2, n3))
