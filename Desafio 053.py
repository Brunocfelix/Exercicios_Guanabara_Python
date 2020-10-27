"""Desafio 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
Exemplo:   APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA"""
frase = str(input('Digite uma frase: ')).strip().upper()    # Desconsidero espaços antes e depois e deixo maiúsculo.
palavras = frase.split()                                    # Transformo a frase em uma lista.
junto = ''.join(palavras)                                   # Junto todos os itens da lista, sem espaço ('').
inverso = ''                                                # Inverso Iniciou como vazio.
for letra in range(len(junto) - 1, -1, -1):                 # len -1 = está contando meus itens do junto, como valores,
                                                            # e não strings, e está contando todos eles, diminuindo
                                                            # um, no final, se tiver 20, começará do 19; -1 pois ao
                                                            # invés de contar até o 0 (primeiro espaço), está contando
                                                            # do segundo, e -1 novamente, por estar de trás pra frente.
    inverso += junto[letra]                                 # inverso recebe ele mesmo e depois o junto contendo o for.
print(junto, inverso)                                       # mostra os itens do junto, e também o inverso.
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
