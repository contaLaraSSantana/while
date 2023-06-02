    #Crie um programa que leia dois valores e mostre um menu na tela:
    #1 - Somar
    #2 - Multiplicar
    #3 - Subtrair
    #4 - Divisão
    #5 - Sair do Programa

num1 = 0
num2 = 0
adicao = num1 + num2
sub = num1 - num2
multi = num1 * num2

while True:
     num1 = int(input("Digte o primeiro número:"))
     num2 = int(input("Digte o primeiro número:"))
     calcular = int(input("\nQual conta irá realizar?(adição-1\nmultiplicação-2\nsubtração-3\ndivisão-4\nsair-5: "))
     if calcular == 1:
         print('A operação escolhida foi adição e o resultado é',adicao)
     if calcular == 2:
         print('A operação escolhida foi multiplicação e o resultado é',multi)
     if calcular == 3:
         print('A operação escolhida foi subtração e o resultado é', sub)
     if calcular == 4:
         print('A operação escolhida foi divisão e o resultado é', num1/num2)
     if calcular == 5:
         print('Obrigado por utilizar esse código!')