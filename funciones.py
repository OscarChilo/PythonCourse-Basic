#Usando Funciones
'''
def suma_tres(n):
    print(n+3)

suma_tres(5)
'''
#Usando funciones sin retorno de valor _tabla de multiplicar
'''
def tabla_multiplicar(n):
    for i in range(1,11):
        print(i, ' X ',n,' = ',i*n)
tabla_multiplicar(9)
'''
#Usando funciones con retorno de valores _mostrar cadena
'''
def cadena():
    return 'curso de python'
print(cadena())
'''
#Usando funciones con valor externo
'''
n=5
def mostrar():
    print(m)

m=10
mostrar()
'''
'''
def funcion():
    n=5
    print(n)
funcion()
n=7
funcion()
print(n)
'''
#Usando funciones _con parametros
'''
def suma (n1,n2):
    return n1+n2
respuesta=suma(2,5)
print(respuesta)
'''
#Usando funciones _con parametros y listas
'''
ejemplo=[5,8,6,2,1,7]
def seleccionar(lista):
    impares=[]
    pares=[]
    for i in lista:
        if i%2==0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

pares,impares=seleccionar(ejemplo)
print(pares,impares)
'''
