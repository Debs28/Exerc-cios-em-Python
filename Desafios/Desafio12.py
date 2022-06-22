#Faça um algoritmo que leia o preço de um produto r mostre seu novo preço com 5% de desconto.
valor = float(input('Digite o valor do produto? R$'))
desconto = valor - (valor * 5 / 100)
print('O valor do seu produto que custava R${:.2f}, com desconto de 5% custará de R${:.2f}'.format(valor, desconto))

