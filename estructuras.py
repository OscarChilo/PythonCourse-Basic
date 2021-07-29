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

numero=int(input('Ingrese un numero para generar la tabla: '))
i=0
while i<=15:
    print(numero," x ",i," = ",(numero*i))
    i=i+1
