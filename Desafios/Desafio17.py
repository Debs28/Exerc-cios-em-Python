"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo, calcule e mostre o comprimento da hipotenusa.
"""
"""
CO = float(input("Comprimento do cateto oposto: "))
CA = float(input("Comprimento do cateto adjacente: "))
HIP = (CO ** 2 + CA ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(HIP))

"""

#Outra forma de fazer o exercício
from  math import hypot

CO = float(input("Comprimento do cateto oposto: "))
CA = float(input("Comprimento do cateto adjacente: "))
HIP = hypot(CO, CA)
print('A hipotenusa vai medir {:.2f}'.format(HIP))