while true: 
    try:
        number = int(input("ingresa un numero: "))

        if 10 <= number <=25:
            print("estas en el rango")
            break
        else:
            print("estas fuera del rango")
    except ValueError:
         print("error, ingresa un numero valido")
    except KeyboardInterrupt:
        print("\noperacion cancelada por el usuario")
        break

print('saliste del bucle')


