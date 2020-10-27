'''Desafio 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

s = str(input('Informe seu sexo: [M/F] ')).upper()[0].strip()
while s not in 'MmFf':
    s = str(input('Dados Inválidos. Por favor, informe seu sexo: [M/F] ')).upper()[0].strip()
print('Sexo {} registrado com sucesso'.format(s))


