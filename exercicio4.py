# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final mostre:
# -Qual é o total de gasto na compra.
# -Qual o nome do produto mais caro

maisCaro = 0
nomeCaro = ""
total = 0

while True:
    produto = input('Digite o nome do produto que gostaria de comprar: ')
    valor = float(input('Qual o valor do produto: '))
    if valor >maisCaro:
        maisCaro = valor
        nomeCaro = produto
    total += valor
    c = input('Deseja continuar?(s/n): ')

    if c != "s":
        break
print('O valor da compra foi de:', total, "e o produto mais caro foi o", nomeCaro)

