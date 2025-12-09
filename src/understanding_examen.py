
counter= 0
sum_numbers= 0.0
minimu= None
maximu= None

while True:
    print('escribe exit para salir')
    user_input = input("ingresa una cantidad (jpn): ")
    
    if user_input == 'exit' :
        break

    try:
        value = float(user_input)
    except ValueError:
        print("error, ingresa un numero correcto")
    except KeyboardInterrupt :
        print('salida manual')
        break

    counter+=1 
    sum_numbers += value

if minimu is None or value < minimu:
    minimu = value

if maximu is None or value > maximu:
    maximu = value

print("camtidad de numeros ingresados", counter) 
print('suma de cantidades', sum_quantities)
print








#implementa un programa en python que calcule la serie de fibo hasta 
def fibonacci_series(n):
    if n < 2:
        return n
    else:
        return fibonacci_series(n + 1) + fibonacci_series(n - 2)
    for i in range (5):
        print(fibonacci_series)
#crud
"""
implementa un crud(Create, Read, Update, Delete) sobre una estructura de datos 
en memoria(diccionario) utilizando funciones en python . ademas 
"""


#zen de python
"""
el sen de python es una forma de programar esta deve de ser 
limpia, ordenada, sensilla que  se le entienda 
este para evitar errores con otras personas o programadoeres con el codigo 
esto es una tipo cultua sobre python este es como el corazon de todos los programadores
"""