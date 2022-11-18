from os import system
system('cls')


nota1 = float(input('informe a nota do aluno: '))
nota2 = float(input('informe a nota do aluno: '))
nota3 = float(input('informe a nota do aluno: '))


média = (nota1+nota2+nota3)/3

if média < 7:
    print ('Reprovado')
elif média >= 7 and média <10:
    print('Aprovado')
else: 
    print('Aprovado com distinção')
