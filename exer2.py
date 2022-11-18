from os import system
import random
system('cls')
titulo = 'Jogo da adivinhação'
print(titulo.center(60,'*'))

num = random.randint(1,10)
print(num)
tentativa = int(input('Advinhe o numero de 1 a 10: (0 - para sair)'))
while tentativa > 0:
    if tentativa > num:
        print('é menor, tente de novo')
    elif tentativa <num:
        print('é maior, tente de novo')
    else: 
        print(f'UHUUULL você acertou - {num}')
        break
    tentativa = int(input('adivinho o numero de 1 a 10: (0 - para sair)'))
