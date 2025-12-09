'''
vamos a realizar 

'''

CORRECT_PIN = "1234"
MAX_ATEMPTS = 3
attempt = 0


while attempt < MAX_ATEMPTS:

    user_input = input("Ingresa tu PIN ")
    
    if user_input == CORRECT_PIN:
        print("Acceso concedido")
        break 
    else:
        attempt += 1
        remaining_attempts = MAX_ATEMPTS - attempt
        if remaining_attempts > 0:
            print("ingrersaste un pin no valido .")
            print(f"Te quedan {remaining_attempts} intentos.")
        else:
            print("cuenta bloqueda.")