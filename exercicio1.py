#Escreva um programa que solicite ao usuário uma série de notas
#(números reais) e calcule a média dessas notas. O programa deve parar de solicitar
# notas quando o usuário digitar um valor negativo.

media = 0
soma = 0
qnt = 0
while True:
    nota = int(input("Digite a nota(para parar de adicionar digite um número negativo): "))
    qnt +=1
    soma += nota
    if nota < 0:
        print("O valor é negativo, vamos a média")
        media = soma / qnt
        print('A média foi de ', media)
        break



