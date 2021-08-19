#Desenvolva um programa que receba duas notas de um aluno 
# e calcule sua média.

nota_um = (float(input('digite a primeira nota: ')))
nota_dois = (float(input('digite a segunda nota: ')))
media = round((nota_um + nota_dois)/2 , 2)

print(f'media das notas: {media}')