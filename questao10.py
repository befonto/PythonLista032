'''
Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos
e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores.
'''

a = int(input("Insira aqui o número total de eleitores do município: "))
b = int(input("Aqui, insira o número de votos brancos: "))
c = int(input("Aqui, o número de votos nulos:"))
d = int(input("E, por último, insira aqui o número de votos válidos: "))

a1 = (b / a) * 100
b1 = (c / a) * 100
c1 = (d / a) * 100

print("")

print("O percentual de votos brancos é de", a1, "%, de votos nulos é de", b1, "% e o votos válidos é de", c1, "%.")
Insira o preço de custo de um produto: 100
Insira o percentual de acréscimo: 10
O valor de venda do seu produto será de R$ 110.0