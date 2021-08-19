#Leia um número, mostre seu dobro, triplo, e raíz quadrada.

numero = int(input('digite um número: '))

dobro = numero * 2
triplo = numero * 3
raiz = round(numero ** (1/2))

print(f' Número: {numero}\n Dobro: {dobro}\n Triplo: {triplo}\n Raiz Quadrada: {raiz}')