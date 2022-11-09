#trabalhando com textos - variavel da class str

#alt + shift + A - para adicionar comentarios automaticos (selecionar texto antes)

from os import system
#para importar bibliotecas - from "n" import "y"  (n - para biblioteca, y - para ação/comandos da biblioteca)
system('cls')
Nomecompleto = input('Informe seu nome completo: ')
print(Nomecompleto)

#tamanho da string | total de caracteres 
print ('1. total de caracteres', len(Nomecompleto))

#acessando um caracter a partir da posição 
print('2. o caracter da posição 2 é: ', Nomecompleto[2])

#transformando string em Maiuscula ou minuscula
print('3. texto em maiusculo', Nomecompleto.upper())
print('4. texto em maiusculo', Nomecompleto.lower())
print('5. texto em maiusculo', Nomecompleto.capitalize())

#procurar a posição de um determinado caractere
print('6. posição do caracter espaço: ', Nomecompleto.find(' '))

#fatiar uma string ate uma determinada posição
espaco = Nomecompleto.find(' ')
print('7. Somente o primeiro nome: ' , Nomecompleto[0:espaco])

#substituir um caracter por outro 
print('8. nome sem espaco: ', Nomecompleto.replace(' ', ''))

#verificar somente letras ou letras e numeros
print('9. Tem somente letras? ', Nomecompleto.replace(' ', '').isalpha())
print('10. É alfanumerico? ', Nomecompleto.replace(' ','').isalnum())

#quebrar o texto em partes especificas retornando array 
print('11. quebrar o texto a cada espaço em branco: ', Nomecompleto.split(" "))

#centralizar o texto usando * para completar laterais
print('12. centralizar o texto entre * ')
print(Nomecompleto.center(80,"*"))




