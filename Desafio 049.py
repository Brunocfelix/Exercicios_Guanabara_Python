#Desafio 049: Reaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
n = int(input('Digite um número para sua tabuada: '))
print('=' * 12)
for c in range(1, 11):
    print('{} * {:2} = {:2}' .format(n, c, c*1))
print('=' * 12)
