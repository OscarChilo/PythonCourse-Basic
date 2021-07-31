#ARREGLOS
#Arreglo de multiplos
'''
n=int(input('ingrese el tamaño del arreglo: '))
m=int(input('ingrese el multiplo del arreglo: '))
A=[]
for i in range (1,n+1):
    A.append(i*m)
print(A)
'''
#Arreglo de impares desde una lista
'''
A=[4,5,8,6,2,8]
B=[]

for i in A:
    if i>3 and i%2!=0:
        B.append(i)
print(B)
'''
#Arreglo de numeros aleatorios
'''
import random

def vector_aleatorio(n):

    vector=[0]*n
    for i in range(n):
        vector[i]=random.randint(0,10)
    return vector
print('cuantos numeros aleatorios desea?: ')
cantidad=int(input())
numeros_aleatorios=vector_aleatorio(cantidad)
print(numeros_aleatorios)
'''
