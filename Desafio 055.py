#Desafio 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso.

peso = []
for p in range(1, 6):
    atual = float(input('Peso da {}ª pessoa: '.format(p)))
    peso.append(atual)

    pesomaior = max(peso)
    pesomenor = min(peso)
print('O maior peso lido foi de {}Kg'.format(pesomaior))
print('O menor peso lido foi de {}Kg'.format(pesomenor))





