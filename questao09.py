'''
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias.
'''

a = int(input("Insira aqui sua idade em anos: "))
b = int(input("Insira aqui o número de meses que se passaram desde seu último aniversário: "))
c = int(input("Insira aqui o número de dias que se passram desde o número de meses completos da resposta anterior: "))

con = (a * 365) + (b * 30) + (c)

print(f"A sua idade em dias é de {con}")