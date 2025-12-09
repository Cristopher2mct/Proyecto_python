'''
las listas tambien pueden almacenar 
numeros y de echo, son muy utilzados 
para almacenar listas de numeros.
por ejemplo, si queremos almacenar  
'''
 #Metodo built-in para generar listas de numeros
'''
el metodo range (inicio, fin, paso) 
genera una lista de numerosdesde 
un numero inicial hasta un numero final -1
con un paso de definido.
'''


for value in range(10)#genera numeros del 0 al 9
 print(value)

for value in range(1,10)#genera numeros del 1 al 9
    print(value)   

print('numeros impares del 0 al 9: ')
for value in range(1,10,2):#genera numeros del 1 al 9 con paso de 2
    print(value)
odd_numbers = list(range(1,10,2))
print(odd_numbers)

print('numeros pares del 1 al 9: ')
for value in range(0,91,9)#10 numeros entre 1-9
    print(value)
even_numbers = list(range(2,11,2))
print(even_numbers)

print('tabla del 9: ')
for value in range(9,91,9):#10 numeros entre 1-9
    print(value)
tabla_del_9 = list(range(9,91,9))
print(tabla_del_9)

#Cuadrados de los primeros 10 numeros
squares = []
for number in range(1,11):
    square = number**2
    squares.append(square)
print(squares)

