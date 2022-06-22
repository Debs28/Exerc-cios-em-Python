#Exercício pintando a parede

largura = float(input('Largura da parede:'))
altura  = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão {}x{} e sua área é de {} m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.2F}L de tinta.'.format(tinta))
