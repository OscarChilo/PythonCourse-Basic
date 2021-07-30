#si numero es negativo o positivo
'''
a=int(input('ingrese un numero entero: '))
if a>0:
    print('el numero es positivo')
else:
    print('el numero es negativo')
'''
#hallar el  numero mayor de dos numeros
'''
a=int(input('ingrese un numero '))
b=int(input('ingrese un numero '))
if a>b:
    print('el numero  mayor es: '+str(a))
else:
    print('el numero mayor es: '+str(b))
'''
#calcular si el numero es par o impar
'''
a=int(input('ingrese un numero'))
if a%2==0:
    print('el numero {} par '.format(a))
else:
    print('el numero es impar')
'''
#calcular si ele numero es positivo, negativo o neutro
'''
numero=int(input('ingrese un numero entero'))
if numero<0:
    r='es negativo'
else:
    if numero>0:
        r='es positivo'
    else:
        r='es neutro'
print(r)
'''
#calcular si la nota es reprobatorio, aprobado, muy bien, excelente
'''
nota=float(input('INGRESE UNA NOTA: '))
if nota<10.5 and nota>=0:
    r='esta reprobado'
elif nota>=10.5 and nota<14:
    r='esta aprobado'
elif nota>=14 and nota<17:
    r='esta muy bien'
elif nota>=17 and nota<21:
    r='esta excelente'
else:
    r='la nota debe ser entre 0 y 20'

print(r)
'''
#uso de while_ suma de los 6 primeros numeros
'''
suma=0
i=1
while (i<=6):
    suma+=i
    i=i+1
print(suma)
'''
#uso de while_ generar una tabla de multiplicar
'''
numero=int(input('Ingrese un numero para generar la tabla: '))
i=0
while i<=15:
    print(numero," x ",i," = ",(numero*i))
    i=i+1
'''
#uso de for _calcular la cantidad de vocales
'''
palabra=str(input('introduce una palabra para calculas sus vocales: '))
vocales='aeiouAEIOU'
contador=0
for i in palabra:
    if i in vocales:
        contador=contador+1
print('la cantidad de vocales en ',palabra,' es ',contador)
'''
#tabla de multiplicacion con range
'''
n=int(input('Ingrese un numero: '))
for i in range(1,11):
    print(n,' x ',i,' = ',n*i)
'''
#mayor que el anterior usando range
'''
valor=int(input('ingrese la cantidad de numeros qie va ingresar: '))
if valor<1:
    print('error')
else:
    primero=int(input('ingrese el primer numero: '))

    for i in range(valor-1):
        numero=int(input('ingrese numero: '))
        if numero<primero:
            print('el numero no es mayor que el primero')
    print('gracias por su colaboracion')
'''
#mostrar los primeros numeros descendientes
'''
numero=int(input('Ingrese un numero: '))
for i in range(numero,0,-1):
    print(i)
'''
#sumas los primeros numeros con range
'''
numero=int(input('ingrese un numeros: '))
suma=0
for i in range(0,numero+1,1):
    suma=suma+i
print(f'la suma de los primeros numeros de {numero} es: ',suma)
'''
#hallar el factorial de un numero con range
'''
numero=int(input('ingrese un numero: '))
producto=1
for i in range(1,numero+1,1):
    producto=producto*i
print(f'el factorial de {numero} es: ',producto)
'''
#generar multiplos de tres de los primeros numeros n
'''
numero=int(input('ingrese un numero: '))
for i in range(1,numero+1,1):
    if i%3==0:
        #print(i)
        print(i,end='-')
'''
#calcular series 432143214....
'''
n=int(input('ingrese la cantidad de series de 4321: '))
count=0
star=4
while count<n:
    print(star)
    if star>1:
        star=star-1
    else:
        star=4
    count=count+1
'''
#calcular la serie sde letras 

n=int(input('ingrese la cantidad de series de la forma ABABAB....: '))
count=0
l='A'
while count<n:
    print(l,end='')
    if l=='A':
        l='B'
        
    else:
        l='A'
        
    count=count+1