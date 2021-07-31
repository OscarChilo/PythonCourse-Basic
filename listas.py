#identificar numeros impares y pares

#normal
'''
n1=int(input('Ingresar numero: '))
n2=int(input('Ingresar numero mayor o igual: '))
for i in range(n1,n2+1):
    if i%2==0:
        
        print(i,' par')
    else:
        print(i,' impar')
'''
    #con CONTINUE (saltea cuando la sentencia se cumple)
'''
    n1=int(input('Ingresar numero: '))
    n2=int(input('Ingresar numero mayor o igual: '))
    for i in range(n1,n2+1):
        if i%2==0:
            continue #saltea la sentencia
            print(i,' par')
        else:
            print(i,' impar')
'''
    #con BREACK(termina la ejecucion de la operacion cuando se cumple la sentencia)
'''
    numero=int(input('ingrese un nummero: '))
    for i in range(1,numero+1):
        print(i)
        if i%5==0:
            break
'''    
#Usando METODOS, hallar elm maximo numero de un lista
'''
lista=[1,5,8,12,4]
print(max(lista))
'''
#Usando METODOS, agregar un nuevo elemento
'''
lista=[5,8,81,6]
print(lista)
lista.append(10)
print(lista)
'''
#Usando METODOS, ordenar una lista
'''
lista=[25,23,45,15,12,12]
print(lista)
lista.sort()
print(lista)
'''
#Usando METODOS, mostrar la lista al reverso
'''
lista=[12,45,25,36]
print(lista)
lista.reverse()
print(lista)
'''