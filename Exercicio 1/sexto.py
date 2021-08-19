#Faça um programa que mostre a soma de dois valores, e depois 
# mostre o antecessor e o sucessor do mesmo.

valor_1 = int(input('Digite um número: '))
valor_2 = int(input('Digite outro número: '))

valor = valor_1 + valor_2
antecessor = valor - 1
sucessor = valor + 1

print(f' Numero: {valor}\n Antecessor: {antecessor}\n Sucessor: {sucessor}')