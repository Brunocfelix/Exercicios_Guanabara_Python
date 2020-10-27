"""Desafio 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos."""
c = ch = cf = 0
while True:
    sexo = ' '
    continuar = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' * 30)
    if idade >= 18:
        c += 1 #Contador de idade
    if sexo == 'M':
        ch += 1 #Contador Masculino
    if sexo == 'F':
        cf += 1 #Contador Feminino
    continuar = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        print(f'Total de pessoas com mais de 18 anos: {c}')
        print(f'Ao todo temos {ch} rapaz(es) cadastrado(s)')
        print(f'Temos {cf} mulher(es) com menos de 20 anos')
        break
    print('-' * 30)
    while continuar not in 'SN':
        continuar = str(input('Não entendi a sua resposta! Por favor, repita.\n'
                              'Quer Continuar? [S/N] ')).strip().upper()[0]

