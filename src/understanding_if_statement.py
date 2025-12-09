cars = ['audi', 'bmw', 'chevrolet', 'corvette', 'tesla']

for car in cars :
    if car == 'bmw'or car == 'tesla' or car == 'audi':
        print(car.upper())
    else:
        print(car)

print('----condiconal----')
#condicionales : el condicional es el corazon de un if
#condicional true
car = 'bmw'
print(car == 'bmw') # true"")


car_2 = 'Audi'
print(car_2 == 'audi') # false

car_2 = 'Audi'
print(car_2.lower() == 'audi') #salida -> true

#condicional != para determinar desigualdad
requested_topping = 'mushrooms' 
if requested_topping != 'anchovies': #-> true
    print("Hold the anchovies!")

#comparaciones numericas
age = 18 # -> int
print(age == 18) # true

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")  

age = 19
print(age < 21) # true
print(age <= 21) # true
print(age > 21) # false
print(age >= 21) # false

#multiples condiciones
age_0 = 22
age_1 = 18 