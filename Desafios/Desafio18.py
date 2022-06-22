
import math
angulo = float(input('Digite o ângulo:'))
Seno = math.sin(math.radians(angulo))
Cos = math.cos(math.radians(angulo))
Tang = math.tan(math.radians(angulo))

print('O ângulo de {} tem o SENO de {:.2f} '.format(angulo, Seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, Cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, Tang))

#outra forma de fazer

from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo:'))
Seno = sin(radians(angulo))
Cos = cos(radians(angulo))
Tang = tan(radians(angulo))

print('O ângulo de {} tem o SENO de {:.2f} '.format(angulo, Seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, Cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, Tang))
