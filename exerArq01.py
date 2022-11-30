from os import system
import os.path, datetime
system('cls')


arquivo = 'produtos.csv'
if os.path.isfile(arquivo):
    produtos = open(arquivo,'r', encoding='utf-8') #utf - trabalhar com acentos
    tamanho = os.path.getsize(arquivo)
    dataModificacao = os.path.getatime(arquivo)
    print(f'data de modificacao: {datetime.datetime.fromtimestamp(dataModificacao)}')
    print(f'Tamanhodo arquivo (bytes): {tamanho}')