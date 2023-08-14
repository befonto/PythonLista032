'''
Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metros.
'''

# import math < isso precisa aparecer ao digitar o "math.pow()"

a = float(input("Insira aqui seu peso: "))
b = float(input("Insira aqui sua altura: "))

imc = a / (b * b)
# outro modo > imc = peso / math.pow(a, 2)


print(f"Seu IMC é de {imc:.0f}") # para controlar o número de dígitos depois da vírgula, nesse caso número redondo





