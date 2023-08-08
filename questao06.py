'''
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês.
'''

a = input("Insira aqui seu nome: ")
b = int(input("Aqui insira seu salário fixo: "))
c = int(input("Aqui insira seu total de vendas efetuadas nesse mês, em dinheiro: "))

com = 0.15

print(a, "seu salário fixo é de", b, "sua comissão é de R$", c * com, ", e seu salário completo será de R$", b + (c * 0.15))