#Diccionario de edades: donde los nombres son claves y las edades son valores
'''
edades={'lara':12,'paola':14,'maria':45,'mariana':15,'luis':47}
print(edades['maria'])#muestra la edad de maria
edades['maria']=19 #agrega nueva edad
print(edades)#muestra toda la lista
'''
#Uso de funciones en  diccionarios

edades={'lara':12,'paola':14,'maria':45,'mariana':15,'luis':47}
#rint(type(edades))        #muestra el typo de dato qu almacena
#print(edades.clear())     #limpia todos los datos de la lista
#edades2=edades.copy()     #crea otra lista copiando la anterior
#print(edades2)   
#valor=edades.get('maria') #halla el valor a partir de una llave 
#print(valor)
#pares=edades.items()      #convierte las claves y sus valores en elementos pares
#print(pares)               
#claves=edades.keys()      #extrae solo las claves en una lista
#print(claves)

dic1={'a':1,'b':2,'c':3,'d':4}
dic2={'d':5,'e':6,'f':7}

#UPDATE: se actualiza el diccionario dic1 con el diccionario dic2
'''
dic1.update(dic2)
print(dic1)
'''
#VALUEs: Retorna los valores de todas las claves de la lista
'''
valores=dic1.values()
print(valores)
'''
#POP: para eliminar un elemento a partir de una clave
'''
valor=dic1.pop('c')
print(valor)
print(dic1)
'''
