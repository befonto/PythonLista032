'''
Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
'''


a = int(input("Insira o preço de custo de um produto: "))
b = int(input("Insira o percentual de acréscimo: "))
c = b / 100

print("O valor de venda do seu produto será de R$", (a * c) + a ,)
