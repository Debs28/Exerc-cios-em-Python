nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a primeira nota: '))
P1 = 0.4
P2 = 0.6

mediaPond = ((P1 * nota1) + (P2 * nota2)) / 1
print('A média ponderada entre {} e {} é igual a {}.'.format(nota1, nota2, mediaPond))


