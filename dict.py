from multiprocessing import current_process


alien_0 = {
    'color': 'green',
    'points': 5
}

alien_1 = {
    'color': 'yellow',
    'points': 6
}

alien_2 = {
    'color': 'red',
    'points': 3
}

aliens = [alien_0, alien_1, alien_2]

print(aliens)

for alien in aliens:
    for key, value in alien.items():
        print(key, value)

# looping through all values in a dictionary

favorite_languajes = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for languaje in favorite_languajes.values():
    print(languaje.title())


aliens = []

for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print(".....")

print(f"Total number of aliens: {len(aliens)}")

pizza = {
    'crust': 'thick',
    'topping': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['topping']} -crust pizza")

for topping in pizza['topping']:
    print(f"{topping}")

# a dictionary in a dictionary

nested_dict = {'dictA': {'key_1': 'value_1'},
               'dictB': {'key_2': 'value_2'}}

print(nested_dict['dictA']['key_1'])

# using a flag

prompt = "Enter 'quit' to end the program"

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# moving items from one list to another

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

print(f"{unconfirmed_users}, {confirmed_users}")

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)

print(f"{unconfirmed_users}, {confirmed_users}")


# removing all instances of specific values from a list

pets = ['dog', 'cat', 'dog', 'cat', 'rabbit', 'cat']

print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
