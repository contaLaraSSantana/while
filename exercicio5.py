#.Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
# 'M'ou 'F'. Caso esteja errado peça a digitação novamente até ter um valor correto.

while True:
    genero = input('O genero do usuário é (M ou F): ')
    if genero != "M" or "F":
        print('Digitação errada, dite novamente novamente')