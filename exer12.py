from os import system
#para importar bibliotecas - from "n" import "y"  (n - para biblioteca, y - para ação/comandos da biblioteca)
system('cls')
#os - system biblioteca que faz a limpeza do terminal (cls é clear para o Windows, no linux e Mac e clear)
import random
#random gera numeros aleatórios entre um intervalo (apenas numeros inteiros)


#print(random.randint(0,10))

num = random.randint(0,100)

#o numero escolhido é par ou impar

ale = random.randint(0,100)
print(ale)


resto = ale % 2 
if resto ==0:
    print(f'é numero par:{resto} ')
else print((f'é numero impar:{resto} '))


#o numero escolhido é <> que 50? (é mais perto do 100 ou de 0)

if num > 50: 
    print('o numero escolhido esta mais perto do 100')
else: print('o numero escolhido esta mais perto do 0')







#o numero escolhido é primo?









