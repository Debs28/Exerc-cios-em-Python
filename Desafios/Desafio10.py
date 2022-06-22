#Conversor de meoedas

real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 5.45
print('Com R${:.2f} você comprar US${:.2f}'.format(real, dolar))