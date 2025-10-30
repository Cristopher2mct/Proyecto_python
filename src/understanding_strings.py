"""
un string es de manera sencilla una serie
 de caracteres. en python, todo lo que se encuentre
 detro de comillas simples(' ') o dobles (" ")
 sera considerado un string.

 Ejemplos:
        "Esto es un string"
        'Esto tambien es un string'

    'Le dije a un amigo "Python es mi lenguaje favorito" '
    "El lenguaje 'Python' lleva el nombre por monty python, no por la serpiente"

"""

name = "clase de programacion"
print (name) 

# title
print(name.title())

print(name)

"""
Un metodo es una accion que python
puede realizar en un fragmento de datos
o sobre una a+variable de datos
    
    El punto . despyes de una variable 
seguido del metodo title () dice que
se tiene que ejecutar el metodo title()
de la variable name.
    
    Todos los metodos van seguidos de parentesis
por que en ocaciones necesitan informacion adicional 
para funcionar, la cual iria dentro de los parentesis
En esta ocacion, el metodo .title() no requiere informcacion 
adicional para funcionar.
"""

print("metodo upper:", name.upper())
print("Metodo lower:", name.lower())

#Concatenacion de STRINGS
first_name = "charly"
last_name = "mercury"
full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())


#Whitespace
"""
Un whitespace se refiere a cualquier caracter que no se 
imprime, es decir, un espacio, tabuladores y finales de linea

"""
print("Whitespace Tabulador")
print("python")
print("\tpython")
print("\t\tpython")

print("whitespace Saalto de linea")
print("Languaje \n\tPython\nC\n\tJavascript")

#Eliminacion de espacios en blanco
programming_languajes = " python "
print(programming_languajes)
print(programming_languajes.rstrip())
print(programming_languajes.lstrip())
print(programming_languajes.strip())

#Syntax error con string
message = 'Una fortaleza de python es su comunidad'
print(message)
message = "una fortaleza de "python" es su comunidad"
print (message)