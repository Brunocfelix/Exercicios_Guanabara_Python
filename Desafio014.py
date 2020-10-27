# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.
c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32        # Ordem de precedência
print('A temperatura de {}ºC corresponde a {}ºF!' .format(c, f))
