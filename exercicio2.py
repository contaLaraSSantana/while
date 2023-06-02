#Escreva um programa que solicite ao usuário que digite uma série de números
# e, em seguida, exiba a soma apenas dos números pares digitados.
# O programa deve parar quando o número 0 for digitado.

soma = 0
qnt = 0
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        print('A soma dos números pares digitados foram',soma)
        break
    elif num % 2 == 0:
        soma += num