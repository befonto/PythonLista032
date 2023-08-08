'''
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom.
'''

a = float(input("Insira aqui o valor da conta a ser pago: "))

gorjeta = 1.0

fim = a + (a * gorjeta)

print("O valor final a ser pago com acréscimo de 10% da gorjeta será de: R$", fim)