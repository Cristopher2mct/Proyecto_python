'''
slicing
'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('lista original', players)

print('slice de lista original', players[0:3])#del indice 0 al 2
print('slice de lista original', players[1:4])#del indice 1 al 3
print('slice de lista original', players[:4])#del indice 0 al 3
print('slice de lista original', players[2:])#del indice 2 al final
print('slice de lista original', players[-3:])#ultimos 3 elementos
print('slice de lista original', players[-3:-1])#del indice -4 al -2
print('slice de lista original', players[5:2])#de inicio a fin

'''
Slicing en un for
'''

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('aqui se precentan los primeros 3 jugadores del equipo')
for player in players [0:3]:
    print(player.title())

'''
    copiando una lista 
'''
my_foods = ['pizza', 'tacos', 'flautas', 'gorditas']
#my_food_copy = my_foods #Error: esta no es la manera de copiar lista 
my_foods_1 = my_food [:]
my_foods_2 = my_food.copy()
my_foods_3 = list(my_foods)