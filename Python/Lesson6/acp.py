age = int(input("Enter your age: "))
can_swim = input("Can you swim? (yes/no): ")
adult = input("Are you with an adult? (yes/no): ")

if age >= 12 and can_swim == "yes":
    print("You can enter the deep end.")
elif age < 12 and can_swim == "yes" and adult == "yes":
    print("You can enter the shallow end with an adult.")
else:
    print("You cannot enter the pool.")