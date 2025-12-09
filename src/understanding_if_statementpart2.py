age = 0

try:
    age = int(input('escribe tu edad: '))
except:
    age = -1
    print('ERROR-ingresaste un caracter no valido puñetas')
 
 # <>
if age > 100:
    print('tiene mas de un siglo') 
elif age >= 18 and age <= 100 :
    print('eres mayor de edad')
elif age >=0 and age <18: 
    print('eres menor de edad')
else:
    print('tuviste un error puñetas pusiste un negativo pendejo ')


print("holi charly")

# ejercicio 
if age <= 4:
    print("la entrada es gratuita") 
elif age > 18 and age < 4 :
    print('la entrada cuesta $200')
elif age <=18: 
    print('la entrada cuesta $400')
else:
    print('introduce tu edad bien ')

#Multiple if 
guisos = ['desebrada', 'asado', 'salsaverde', 'posole' ]
if 'asado' in guisos:
    print('si hay asado')
else:
    print('no hay asado')
if 'tamales' in guisos:
    print('hay tamales')
else:
    print('no hay tamales')
if 'salsa verde' in guisos:
    print('si hay salsa verde')
else:
    print('no hay salsa verde')

#utilizando varias listas
guisos_disponibles = ['salsaverde', 'desebrada', 'mole']
guisos_a_ordenar = ['desebrada', 'caldo de iguana']

print('que guisos quieres ordenar?')
for guiso in guisos_a_ordenar:
    print(f'deseo{guiso}')
    if guiso in guisos_disponibles:
        print(f'si tenemos {guiso}')
    else:
        print('no tenemos de ese guiso')
print('realizando pedido...')
