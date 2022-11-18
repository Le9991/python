from os import system
system('cls')
titulo = 'Conversor de Medidas'
print(titulo.center(80, '*'))
medida = float(input('informe a medida em centimentros: '))

print('\nEscolha para que unidade deseja converter')
print('1 - polegada\n2 - Pé\n3 - jarda')


menu = input('Opção: ')

valorPolegada = 2.54
ValorPés = 30.48
ValorJarda = 91.44

if menu == '1':
    polegada = medida / valorPolegada
    resultado = str(f'{medida:.4f} centimeros correspondem a {polegada:.4f} polegadas')
elif menu == '2':
    pés = medida / ValorPés
    resultado = str(f'{medida:.4f} centimeros correspondem a {pés:.4f} pés')
elif menu == '3':
    Jarda = medida / ValorJarda
    resultado =  str(f'{medida:.4f} centimeros correspondem a {Jarda:.4f} Jarda')
else:
    resultado = str(f'Você não escolheu uma das opções validas')


print (resultado)
    
