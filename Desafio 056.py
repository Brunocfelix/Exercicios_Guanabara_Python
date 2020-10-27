"""Desafio 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
• A Média de idade do grupo.
• Qual é o nome do homem mais velho.
• Quantas mulheres têm menos de 20 anos."""
somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = ''
totalmulheres20 = 0

for p in range(1, 5):
    print('-' * 5, '{}ª Pessoa'.format(p), '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulheres20 += 1

media = somaidade / 4.0
print('A Média de idade do grupo é de {:.1f} anos.'.format(media))
print('O Homem mais velho tem {} anos, e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo existe/existem {} mulhere(s) com menos de 20 anos.'.format(totalmulheres20))