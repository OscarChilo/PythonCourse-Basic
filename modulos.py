#MODULOS
#modulo math tiene varias funciones numericas en general
from math import factorial
#modulo random, propiedades aleatorias
from random import choice    #propiedad de elementos aleatorios
from random import randrange #propiedad de numeros aleatorios
from datetime import date    #propiedad de tiempo o fecha
from fractions import Fraction
'''
a=factorial(5)
print(a)

b=choice(['cara','sello'])
print(b)

c=randrange(9)
print(c)
'''
hoy=date(2021,7,31)
fin_año=date(2021,12,31)
dias_faltan=(fin_año-hoy).days
print('faltan ',dias_faltan,' dias')

x=Fraction(4,5)
y=Fraction(6,8)
print(x+y)
