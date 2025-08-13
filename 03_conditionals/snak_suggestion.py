snack = input("Enter your preferred snack(Cookies/Samosas): ").lower()

if snack == "cookies" or snack == "samosas":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print("Sorry, we only serve Cookies or Samosas with tea")