#Faça um programa que leia um valor, e mostre a sua 
# tabuada do 1 ao 10 na tela.

numero = int(input('Digite um número de 1 a 10: '))

fator = 1

while fator <= 10:
    print(f'{numero} x {fator} = ', numero * fator)
    fator+=1