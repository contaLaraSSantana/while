#Desenvolva um programa que leia vários números até que o usuário digite um
#numero negativo. O programa também encerra se o usuário digita o numero 999
# ,isso deve ser uma condição de parada.

while True:
    num = int(input("Digite um número: "))
    if num == 999:
        print('O número digitado é muito grande')
        break
    elif num < 0:
        print('Números negativos são a condição de parada')
        break
