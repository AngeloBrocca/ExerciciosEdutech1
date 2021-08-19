#Faça um programa que leia um valor em metros, mostre o valor convertido
# em centímetros, e milímetros.

metro = int(input('insira o valor em metros:' ))

centimetro = metro * 100
milimetro = metro * 1000

print(f'Valor do comprimento:\n {metro}m\n {centimetro}cm\n {milimetro}mm')