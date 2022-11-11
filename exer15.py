#faça um programa que receba numeros e informe qual numero é o maior e qual numero é o menor

from os import system
system('cls')
import random

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
if num1 < num2 and num1 < num3:
    print(f'{num1} é o maior')
elif num2 < num1 and num2 < num3:
    print(f'{num2} é o menor')
else: 
    print(f'{num3} é o menor')
