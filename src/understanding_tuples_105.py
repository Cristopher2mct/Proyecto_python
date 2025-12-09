#tuples 
'''
    las tuplas son listas de elemntosque no
    cambian de tamaño.las TUPLAS son INMUTABLES.

    se utilizan los () para definir una tupla.


'''
rectangle_measurements = (200,50) # (largo, ancho)
print(rectangle[0])
print(rectangle[1])

for measure in rectangle_measurements:
    print(measure)

print(dir(rectangle_measurements))# build-in dir

#regresando a las listas
cars['bwm', 'masda', 'porche']
print(cars)
cars[0]'bmw'
cars[1]'porshe'
cars[2]'mazda'
print(cars)

rectangle_measurements = (200,50) # (largo, ancho)
#rectangle_measurements =[0]=300 #No se puede 
#rectangle_measurements =[1]=100 #No se puede
rectangle_measurements = (300,100)
'''
    no podemos modificar una tupla directamente, 
    lo que si podemos hacer es cambiar la signacion
    a una variable que almacena una tupla. 
'''