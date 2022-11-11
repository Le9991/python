#faca um programa que pergunte em que turno você estuda, peça para digitar: 
# M - matutino | V- vespertino | N - noturno
# e imprima a mensagem: 
# "Bom dia", "Boa tarde", "Boa Noite"

from os import system
system('cls')

turno = input('Informe seu periodo: M - Matutino | V - Vespertino | N - Noturno:  ')

if turno.lower() == 'm':
    print ('Bom dia')
elif turno.lower() == 'v':
    print ('Boa tarde')
elif turno.lower () == 'n':
    print ('Boa Noite')
else: 
    print('turno não existe')






