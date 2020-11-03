"""Desafio 073: Crie uma tupla preenchida com os 20 primeiros colocados da tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois, mostre:
A) Apenas os 5 primeiros colocados;
B) Os últimos 4 colocados da tabela;
C) Uma lista com os times em ordem alfabética;
D) Em que posição na tabela está o time da Chapecoense ou São Paulo."""
tabela = ('Internacional', 'Flamengo', 'Atlético-MG', 'Fluminense', 'São Paulo',
          'Santos', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Grêmio', 'Ceará', 'Atlético-GO',
          'Sport Recife', 'Botafogo', 'Bahia', 'Coritiba', 'Bragantino-SP', 'Vasco da Gama',
          'Athletico-PR', 'Goiás')
print('-=' * 20)
print(f'Tabela de Times do Brasileirão no dia 01.11.2020: {tabela}')
print('-=' * 20)
print(f'Os 5 primeiros colocados são: {tabela[0:5]} ')
print('-=' * 20)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 20)
print(f'O São Paulo está na {tabela.index("São Paulo")}ª Posição.')
print('-=' * 20)
