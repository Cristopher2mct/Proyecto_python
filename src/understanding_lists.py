#list
"""
    Las listas son elementos mutables

    Las listas nos permiten almacenar la informacion
    en un lugar, la cantidad que tengan: ya sea 
    pocos elementos o millones de elementos.
    
    se recomineda nombrar una variable del tipo lista
    en plural. 

    En python los corchetes [] definen una lista,
    sus elementos van separados por comas.
    ejemplo:

"""
bicycles=['trek','canondale','readline','specialized','giant']
print(bicycles)

print(bicycles[0].title())

#Los indices comienzan en 0 y terminan en n-1, donde n es el numerode elementos
print(bicycles[4].title())

#Accediendo al ultimo elemento 
print(bicycles[-1].title())#1er er elemento
print(bicycles[-2].title())
print(bicycles[-5].title())#2do elemento

#Utilizado valores de lista 
message = 'mi primera bicicleta fue una ' + bicycles[4].upper() + "."
print(message)

message_f = f'mi primer bicicleta fue una {bicycles[4].title()}.'
print(message_f) 

##agregar elementos a una lista 
print('\n')
print('agregar elemento a una lista')
print(bicycles)

print('metodo de las listas para agregar elementos: list_name.appened(elements)')
bicycles.append('ducatti')
print(bicycles)

'''
    Ejemplo: 

'''
students = ['jesus','josue','andrik','jen','miguel','angi']
print(students)
desired_students = input('¿que estudiantes deseas borrar de la lista?')
students.remove(desired_students.strip().lower())
print(students)
print(desired_students) 
print(desired_students, 'salio de la lista por joto')
students.reverse()
print(students)

print(len(students))

cars = ['kia' ,'ford' ,'tesla' ,'chebrolet' ,'volvo' ]
print(cars)
print(sorted(cars))
sorted_list = sorted(cars)
print('lista original', cars)
print(cars)