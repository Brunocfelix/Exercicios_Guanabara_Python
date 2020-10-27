"""Desafio 070: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário irá continuar.
No final, mostre:
A) Qual é o total gasto na compra;
B) Quantos produtos custam mais de R$1000,00;
C) Qual é o nome do produto mais barato."""
nome = 'LOJA PYBARATO'
fim = ' FIM DO PROGRAMA '
total = cont = preçomaisbarato = atualproduto = c = 0
produtomaisbarato = ' '
print('-' * 30)
print(f'{nome:^30}')
print('-' * 30)
while True:
    continuar = ' '
    produto = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$'))
    total += preço
    if preço >= 1000:
        cont += 1
    if c == 0:
        preçomaisbarato = preço
        produtomaisbarato = produto
    if preço < preçomaisbarato:
        preçomaisbarato = preço
        produtomaisbarato = produto

    continuar = str(input('Quer Continuar? [S/N] ')).upper()[0].strip()
    if continuar == 'S':
        c += 1
    if continuar == 'N':
        print(f'{fim:=^40}')
        print(f'O total da compra foi de R${total:.2f}')
        print(f'Temos {cont} produto(s) custando mais de R$1000.00')
        print(f'O produto mais barato foi {produtomaisbarato}, este produto custou R${preçomaisbarato:.2f}.')
        break
    while continuar not in 'SN':
        continuar = str(input('Não entendi a sua resposta! Por favor, repita.\n'
                              'Quer continuar? [S/N] ')).upper()[0].strip()
