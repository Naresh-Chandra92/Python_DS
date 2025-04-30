import time

print("🧠 Know Your Personality")

print ("✨ Let's discover who you really are with some fun data magic!")

name=input("Enter your name:").strip()
age=int(input("Enter your age:"))
city=input("Enter your city name:").strip()
food=input("Enter your favorite food:").strip()
color=input("Enter your favorite color:").strip()
animal=input("Enter your favorite animal name:").strip()
game=input("Which games your play in your favorite time?").strip()

import time

time.sleep(1)

print("🔍 Doing some analysis")

time.sleep(1)

name_length=len(name)
city_length=len(city)

age_type=type(age)
food_type=type(food)

print(f"Your name has {name_length} characters")
time.sleep(1)
print(f"Your city has {city_length} characters")
time.sleep(1)
print(f"Data type of age is {age_type}")
time.sleep(1)
print(f"Data type of food is {food_type}")


print("🔍 Scanning colors, foods, and animal energies...")

time.sleep(1)

print("💫 Calculating your personality type using complex non-scientific logic...")

time.sleep(1)

print (f"🎉 Hey {name}, here's your fun personality report!")

time.sleep(1)

print(f"🌆 You're from {city}, a place of dreams!")
time.sleep(1)
print(f"🍿 You love {food} and enjoy doing {game}.")
time.sleep(1)
print (f"🎨 You vibe with the color {color} and your spirit animal is the {animal}.")
time.sleep(1)
print(f"📅 You've lived approximately {age*12} months already.")
time.sleep(1)
if age<18:
    print("🧩 You belong to the 'Young Explorer' tribe")
if age>=18 and age <=30:
    print("🧩 You belong to the 'Adventurer' tribe")
if age>30:
    print("🧩 You belong to the 'Wise Owl' tribe")
time.sleep(1)
age_last_digit = age % 10

personality_code = name[:2].upper() + str(age_last_digit) + animal[0].upper() + color[0].upper()
time.sleep(1)
print(f"🔑 Your Personality Code is: {personality_code}")
time.sleep(1)
print("💡 Time to explore more hobbies? You’ve got hidden sparks waiting!")
time.sleep(1)
print("🌈 You are officially certified as: FUNKY AND FABULOUS! 😎")

