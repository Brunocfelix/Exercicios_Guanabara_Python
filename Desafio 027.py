"""DESAFIO 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
nome,separadamente.
Exemplo: Ana Maria de Souza                                      Exemplo: Bruno Campagnoli Félix
Primeiro = Ana                                                   Primeiro = Bruno
Último = Souza                                                   Último = Félix"""
nome = str(input('Digite Seu Nome Completo: ')).strip()
print('Muito prazer em te conhecer !')
n = nome.split()
print('Seu primeiro nome é {}' .format(n[0]))
print('Seu Ultimo nome é {}' .format(n[len(n)-1])) #n[len(n)-1] ele irá ler quantos caracteres tem e subtrair 1,
                                                    #e depois ler seu nome.




