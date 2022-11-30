from Recibo import Recibo
from os import system
system('cls')

novoRecibo = Recibo('Leandra')
novoRecibo.valor = 1,528.99
novoRecibo.descricao('desenvolvimento de sistemas em Python')

print(novoRecibo)
