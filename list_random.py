

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
names_count = len(names)
print(names_count)

randomInt = random.randint(0, names_count -1 )
name_choice = names[randomInt]

while randomInt != 1:
    randomInt = random.randint(0, names_count - 1)
    name_choice = names[randomInt]
    print(f"{name_choice} is going to buy the meal today! ")