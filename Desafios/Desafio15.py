#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar, sabendo que carro custa 60 reias por dia R$0,15 por km rodado.

alg = int(input('Quantos dias alugados?'))
Km = float(input('Quantos Km rodados?'))
preço = (60 * alg) + (Km * 0.15)

print('O total a pagar é de R${:.2f}.'.format(preço))

