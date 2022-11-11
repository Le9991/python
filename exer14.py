from os import system
system('cls')
import random


#variavieis "if" - Se um ou outro verdadeiro
#"else" - falso do if
#"elif" - se condicional 
#"and" se utiliza quando os dois argumentos são verdadeiros e e "or" quando é um ou outro verdadeiro


#faça um programa que receba 3 numeros e informe qual numero é maior

num1 = random.randint(0,100)
num2 = random.randint(0,100)
num3 = random.randint(0,100)

escolhidos = (num1, num2, num3)
print(escolhidos)

if num1 > num2 and num1 > num3:
    print(f'{num1} é o maior')
elif num2 > num1 and num2 > num3:
    print(f'{num2} é o maior')
else: 
    print(f'{num3} é o maior')
