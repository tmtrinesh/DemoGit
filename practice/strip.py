#to remove spaces
favourite_langauge = ' python'
favourite_langauge.rstrip()
favourite_langauge.lstrip()
favourite_langauge.strip()
print(favourite_langauge)

print(.1+.1)
print(2+.1)
print(2*.01)

age=23
message = "Happy" +" " + str(age) + "rd Birthday"
print(message)

print(3/2)
print(3.0/2)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a  " + bicycles[1].title() + "."
print(bicycles)
print(bicycles[0].title())
print(message)


##listfunctions append index insert


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(0, 'nissan')
print(motorcycles)
del motorcycles[0]
motorcycles.remove('yamaha')
print(motorcycles)
print(motorcycles[2])
print(motorcycles[-2])

##Sort and length fun###
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
print("\nHere is the sorted list:")
print(cars)
cars.sort(reverse=True)
print("\nHere is the reverse list :")
print(cars)
print(len(cars))


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")

for value in range(1,5):
 print(value)

numbers=list(range(1,6))
print(numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
##Range
squares = [value**2 for value in range(1,11)]
print(squares)
###statements#####
cars = ['audi','bmw','subaru','sunny']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

for i in range(3,13):
    print("{:3d} {:4d} {:5d}".format(i, i * i, i * i * i))
##############################################################
print(sum({-10: 'x', -20: 'y', -30: 'z'}))
#Calculate sum of numbers in dictionary

#######Iterating through Lists
sharks = ['hammerhead', 'great white', 'dogfish','frilled', 'bullhead', 'requiem']
for item in range(len(sharks)):
    sharks.append('shark')
print(sharks)

sammy = 'Sammy'
for letter in sammy:
    print(letter)

num_list = [1, 2, 3]
alpha_list = ['a', 'b', 'c']
for number in num_list:
    print(number)
    for letter in alpha_list:
        print(letter)


list_of_lists = [['hammerhead', 'great white','dogfish'],[0, 1, 2],[9.9, 8.8, 7.7]]
for list in list_of_lists:
    print(list)

list_of_lists = [['hammerhead', 'great white','dogfish'],[0, 1, 2],[9.9, 8.8, 7.7]]
for list in list_of_lists:
    for item in list:
        print(item)

###########
print(r"\nYellow")
print(len(""))



