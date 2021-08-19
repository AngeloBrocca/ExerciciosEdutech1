#Faça um programa que receba um valor, e traga informações sobre esse
#  valor, dizendo se é alfanumérico, numérico e etc.

frase = input('Digite alguma coisa: ')
valor = str(frase)

if valor.isalnum() == True:
    print('O valor é alfanumérico.')
if valor.isnumeric() == True:
    print('O valor é numérico.')
if valor.isspace() == True:
    print('O valor é apenas espaço.')
if valor.isprintable() == True:
    print('O valor é printavel.')
if valor.isidentifier() == True:
    print('O valor é um identificável valido.')
if valor.isalpha() == True:
    print('O valor tem apenas caracteres alfabéticos.')
if valor.isdigit() == True:
    print('O valor tem apenas digitos.')
if valor.isdecimal() == True:
    print('O valor tem apenas decimais.')
if valor.istitle() == True:
    print('O valor segue os requisitos de um título.')
if valor.islower() == True:
    print('O valor tem apenas caracteres minúsculos')
if valor.isupper() == True:
    print('O valor tem apenas caracteres maiúsculos')