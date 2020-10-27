"""Desafio 059: Crie um programa que leia dois valores e mostrar um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep

n = 0
n1 = int(input('Digite o Primeiro Valor: '))
n2 = int(input('Digite o Segundo Valor: '))
print('=-=' * 13)
while n != 5:

    print(' [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos Números \n [5] Sair do Programa')
    n = int(input('>>>>>> Qual é a sua opção? '))
    if n == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é igual a {}'.format(n1, n2, soma))

    elif n == 2:
        mult = n1 * n2
        print('A multiplicação entre {} * {} é igual a {}'.format(n1, n2, mult))

    elif n == 3:
        if n1 < n2:
            maior = n2
        else:
            maior = n1
        print('Entre {} e {}, o maior valor é {}'.format(n1, n2, maior))

    elif n == 4:
        print('Como desejado, informe os Números novamente!')
        sleep(1)
        n1 = int(input('Digite o Primeiro Valor: '))
        n2 = int(input('Digite o Segundo Valor: '))

    elif n == 5:
        print('Finalizando...')
        sleep(2)

        print('Fim do programa! Volte sempre!')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 13)
    sleep(1)







