from os import system
system('cls')
import random

titulo = 'PEDRA |  PAPEL  | TESOURA'
print(titulo.center(60, '#'))

opcao = 's'
contadorjogadas = 0
contadorjogador = 0
contadorcomputador = 0
while opcao.upper()=="S":
    system('cls')
    computador = random.randint(0,2)
    jogador = int(input('''Escolha uma opção para se jogar:
    [0] Pedra 
    [1] Papel
    [2] Tesoura
    Digite  sua escolha:'''))
    

    if jogador > 3:
            resultado = f'Você não escolheu uma opção válida'
    else: 
            contadorjogadas +=1
            pecas = ('Pedra','Papel','Tesoura')
            print(f'Voce escolheu {pecas[jogador]}'),
            print(f'Computador escolheu {pecas[computador]}')
            tabela = ((0,1,-1), (-1,0,1), (1,-1,0))
            jogada = tabela[computador][jogador]
            if jogada == 0:
                resultado = f'deu empate'
            elif jogada == 1:
                resultado = f'Voce ganhou'
                contadorjogador += 1
            elif jogada == -1:
                resultado = f'O computador ganhou'
                contadorcomputador += 1 
    print(resultado)
    opcao = input('Jogar novamente? (S) para sim')

print('Resumo do Jogo'.center(60,'*'))
print(f'Quantidade de jogadas: {contadorjogadas} jogadas')
print(f'voce ganhou {contadorjogador} jogadas')
print(f'Computador ganhou {contadorcomputador} jogadas')