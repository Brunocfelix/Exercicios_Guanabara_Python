#Desafio 048: Faça um programa que calcule a some entre todos os números ímpares que são múltiplos de três e
#que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
