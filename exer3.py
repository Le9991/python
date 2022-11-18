#numeros primos

from os import system
system('cls')

titulo = 'verificador de numeros primos'
print(titulo.center(60, '*'))


while True:
    num = int(input('Digite um numero inteiro: '))
    if num >= 2:
        break
    else: 
        print(f'Informe numero maior ou igual a 2')



resultado = 'O numero é Primo'
i = 2
while i < num: 
    resto = num % i
    if resto == 0:
        resultado = 'O mumero não é primo'
        break
    i += 1

print(resultado)