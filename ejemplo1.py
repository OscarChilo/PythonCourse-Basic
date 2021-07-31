from par import pares
from par import ciclo_pares

b=pares(15)
print(b)

m=int(input('Ingrese un rango: '))
print(f'los pares dentro de 0 y {m} es: ')
for i in ciclo_pares(m):
    print(i)