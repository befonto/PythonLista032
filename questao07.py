'''
A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações.
'''

a = float(input("Insira aqui o valor de sua compra: "))
b = float(input("Aqui, insira o número de prestações escolhidas: "))

conta = a / b

print("O valor das prestações será de R$", conta,)
