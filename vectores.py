#VECTORES Y MATRICES 
#Para trabajar adecuadamente debemos hacer uso de la bibiloteca
#NUMPY, da soporte a matrices y vectores.

import numpy as np

vector=np.array([6,2.3,5,7])
matriz=np.array([[2,5,4],[5,8,9],[4,8,9]])

print('vector: ',vector)
print('matriz: ',matriz)
print('tamaño del vector: ',vector.size)
print('tamaño de la matriz: ',matriz.size)

print(vector.min())     #metodo para el valor minimo
print(vector.argmin())  #metodo para el indice del vallooor minimo
print(vector.prod())    #metodo para hallar le producto de los valores del vector


