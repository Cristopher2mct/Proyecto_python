#vamos a intentar utilizar variables
message = "This is my first program =)"
another_message = "really, really happy"

print(message)
print(another_message)

message_charli = "HOLA amigo Python"

print(message_charli)

print(message_charli)

"""
    Traceback Es un registro de donde el interprete
    tuvo probelmas al interpretar ejecutar su codigo.
    (ejemplo)
    traceback(most recent call last):
    Traceback (most recent call last):
        File "C:\Users\trejo\python_proyect\casa_domotica\src\understanding_variables.py", line 12, in <module>
        print(mesage_charli)
          ^^^^^^^^^^^^^
    NameError: name 'mesage_charli' is not defined. Did you mean: 'message_charli'?
    Variable antes de utilizar o cometimos un error al ingresar 
    el nombre de la variable.
"""

"""
    Ejercicio:

        1.Almacena un mensaje en una variable y imprimelo.
        2.Almacena un mensaje en una variable y imprimelo. 
         luegocambia el valor de tu variable a otro
         mensaje e imprime el nuevo mensaje.
"""

message = "This is my first program =)"
another_message = "really, really happy"

print(message)
print(another_message)