'''
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
'''

a = int(input("Insira aqui seu peso em quilos: "))
b = float(input("Insira aqui sua altura em metros: "))

peso = a * 1000
altura = b * 100

print("Seu peso em gramas é de", peso, "e sua altura em centímetros é de", altura,)
