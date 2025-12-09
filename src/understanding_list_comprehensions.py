'''
squares=[]
for value in range(0,11):
    square = value**2
    squares.append(square)
print(squares)
'''
'''
una list comprehension convina el ciclo for
y la creacion de elementos en una sola linea
y automaticamente agrega cada nuevo elemnt 
a la lista, es decir, sin utilizar el metodo append().
'''
square = [value**2 for value in range(0,11)]

#Para los numeros pares entre el 0 y 100
squares_range = [value for value in range(0,101,2)]

evens_if = [value for value in range(0,101) if value% 2==0]
print(evens_if)
