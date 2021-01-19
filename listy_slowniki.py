cars = ['Audi', 'BMW', 'Honda', 'Hyundai', 'Peugeot', 'Mercedes']
user = ['John', 56.5, 44, True]

print(cars[0:3])
print(cars[-3:-1])
print(cars[-1])

animals = ['dog', 'cat', 'fish']
first_animal = animals[0]
second_animal = animals[1]
print(first_animal)
print(second_animal)

last_animal = animals[-1]
print(last_animal)

animals.append('bee')
animals.append('ant')
animals.append('pig')
print(animals)

print(f'Number of animals is : {len(animals)}')
print(f'Number of users is: {len(user)}')

emails = []
emails.append('a1@example.com')
emails.append('a2@example.com')
emails.append('a3@example.com')
print(emails)

# ---- slownik ----
friend = {
    'first_name': 'Dave',
    'age': 30,
    'hobby': 'music',
    'city': 'Los_Angeles',
    'average_grade': 3.78,
    'favourite_car': 'Toyota'
}

friends_name = friend['hobby']  ##wyciagamy po kluczu
print(friends_name)
print(friend['average_grade'])
friend['average_grade'] = 4.45
print(friend['average_grade'])
friend['favourite_car']= cars[-3]
print(friend)

name1 = {'n': 'Kasia', 'age': 29}
name2 = {'n': 'Ania', 'age': 36}
name3 = {'n': 'Piotrek', 'age': 42}

names = [name1, name2, name3]
print(names)

print(f'Second name is {names[1]["n"]}')