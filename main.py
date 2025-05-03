import time

points = 0

print("🩺 QuickHealth Pro Max – Interactive Symptom Checker")
print("👋 Hello there! Let's check how you're doing today.")
time.sleep(1)

print("Personal Details")
name = input("Please enter your name: ").strip()
age = int(input("Enter your age: "))
gender = input("Enter your gender (male/female/other): ").strip().lower()
city = input("Enter your city: ").strip()

print("🤒 Symptoms & Health Info")
symptoms = input("Select all symptoms you're experiencing (comma separated): fever, cough, fatigue, headache, chest pain, breathlessness: ").lower()
temperature = float(input("Body temperature in Fahrenheit: "))
sick_days = int(input("Number of sick days: "))
smoking = input("Smoking habit (Yes/No): ").strip().lower()
sleep_hour = int(input("Hours of sleep last night: "))
mood = input("Choose from calm, anxious, sad, irritable: ").strip().lower()
pre_existing_conditions = input("Do you have any preexisting conditions (Yes/No): ").strip().lower()

if temperature >= 102 or sick_days > 3:
    points += 3
elif age >= 60 and temperature > 100:
    points += 2
elif sick_days >= 5:
    points += 2
elif symptoms == "fatigue" and age > 30:
    points += 2
elif symptoms == "headache" and temperature > 100:
    points += 2
elif symptoms == "chest pain":
    points += 3
elif symptoms == "breathlessness":
    points += 4
elif smoking == "yes":
    points += 2
elif sleep_hour < 6:
    points += 1
elif mood in ["anxious", "sad", "irritable"]:
    points += 1
elif pre_existing_conditions == "yes":
    points += 2

total_points = points
print("Total Points:", total_points)


time.sleep(2)

print("\n📊 4. Health Risk Result")
if total_points < 3:
    print("🟢 Low Risk")
elif total_points < 6:
    print("🟠 Moderate Risk")
elif total_points >= 7:
    print("🔴 High Risk")


time.sleep(2)

print("\n🩺 5. Personalized Advice")
if gender == "female" and age >= 45:
    print("- Recommend health screening")
elif gender == "male" and smoking == "yes":
    print("- Suggest quitting smoking")
elif sleep_hour < 6:
    print("- Suggest getting more rest")
elif mood == "anxious":
    print("- Suggest relaxation/breathing")
elif pre_existing_conditions:
    print("- Suggest medical attention")

print(f"- Please visit the nearest urgent care center in {city}")


time.sleep(2)

print("\n🧘 6. Mental Health Tip")
if mood == "calm":
    print("Encourage positivity")
elif mood == "sad":
    print("Suggest talking to someone")
elif mood == "anxious":
    print("Teach box breathing")
elif mood == "irritable":
    print("Suggest taking a break")
