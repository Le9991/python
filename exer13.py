#faca um programa que receba 2 numeros e informe qual numero é maior
from os import system
#para importar bibliotecas - from "n" import "y"  (n - para biblioteca, y - para ação/comandos da biblioteca)
system('cls')
#os - system biblioteca que faz a limpeza do terminal (cls é clear para o Windows, no linux e Mac e clear)
import random
#random gera numeros aleatórios entre um intervalo (apenas numeros inteiros)



num1 = int(input('qualquer valor 1: '))
num2 = int(input('qualquer valor 2: '))

if num1 > num2:
    print(f' {num1} é maior que {num2}: ')
else: 
    print(f' {num2} é maior que {num1}: ')
   

num4 = int(input('informe um numero'))
num5 = random.randint(0,100)
if num4 > num5:
    print(f' {num4} é maior que {num5}: ')
else: 
    print(f' {num5} é maior que {num4}: ')


