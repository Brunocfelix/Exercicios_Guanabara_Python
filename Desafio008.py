# Desafio 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros;
# km hm dam m dm cm mm
medida = float(input('Digite um valor em metros: '))
cm = medida * 100                       # centímetros
mm = medida * 1000                      # milímetros
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida {}m corresponde a:\n{:.0f}cm \n{:.0f}mm \n{:.0f}dm' .format(medida, cm, mm, dm))
print('{:.3f}dam \n{:.3f}hm \n{:.3f}km'.format(dam, hm, km))

