from functools import total_ordering
from os import system
system('cls')
titulo = 'Calcular lista de compras'
print(titulo.center(60,'#'))

produtosDesc = []
produtospreco = []
numeroitens = int(input('Informe numero de Itens desejados: '))
for i in range(0,numeroitens):
    nomeProduto = input(f'nome do produto{i+1}: ') 
    precoProduto = float(input(f'Preço do {nomeProduto}'))
    produtosDesc.append(nomeProduto)
    produtospreco.append(precoProduto)

total = 0
for i in range(0,numeroitens):
    print(f'{produtosDesc[i]} - R$ {produtospreco[i]}')
    total += produtospreco[i]
    
   

print(f'Total: R$ {total}')
print(produtosDesc)
print(produtospreco)
