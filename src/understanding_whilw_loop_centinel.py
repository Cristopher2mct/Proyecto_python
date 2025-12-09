'''
    Docstring for understanding_while_loop_centinel

    un programa que :
    - cuente cuantos numeros ingresa el usuario
    -realice la suma de los numeros ingresados
    -me diga cual es el minimo de los numeros ingresados
    -me diga cual es el maximo de los numeros ingresados
'''
counter= 0
sum_numbers= 0.0
minimu= None
maximu= None

while True:
    print('escribe exit para salir')
    user_input = input("ingresa una cantidad (mxn): ")
    
    if user_input == 'exit' :
        break

    try:
        value = float(user_input)
    except ValueError:
        print("error, ingresa un numero valido")
    except KeyboardInterrupt :
        print('salida manual')
        break

    counter+=1 #counter = counter + 1 (contadr)
    sum_numbers += value #sum_numbers = sum_numbers + value (suma)

if minimu is None or value < minimu:
    minimu = value

if maximu is None or value > maximu:
    maximu = value

print("camtidad de numeros ingresados", counter) 
print('suma de cantidades', sum_quantities)
print
