# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1.lower() +  name2.lower()


string_true = "true"
string_love = "love"

total_true = 0
total_love = 0

for element in range(0, len(string_true)):
    total_true = total_true + name.count(string_true[element])
   
for element in range(0, len(string_love)):
    total_love = total_love + name.count(string_love[element])
    
score = str(total_true) + str(total_love)

final_result = ""

if int(score) < 10 or int(score) > 90:
    final_result = f"Your score is {score}, you go together like coke and mentos."
elif int(score) >= 40 and int(score) <= 50:
    final_result = f"Your score is {score}, you are alright together."
else:
    final_result = f"Your score is {score}."

print(final_result)

