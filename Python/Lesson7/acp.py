
print("Welcome to the Holiday Activity Planner!")
print("Choose your holiday type:")
print("1. Beach")
print("2. Adventure")
print("3. Relaxation")

choice = input("Enter your choice: ").lower()

if choice == "beach" or choice == "1":
    print("You have chosen a Beach Holiday!")
    activity = input("Do you prefer swimming or sunbathing? ").lower()

    if activity == "swimming":
        print("Your activity plan: Enjoy swimming and water sports!")
    elif activity == "sunbathing":
        print("Your activity plan: Relax on the beach and enjoy the sunshine!")
    else:
        print("Your activity plan: Enjoy a peaceful walk along the beach!")

elif choice == "adventure" or choice == "2":
    print("You have chosen an Adventure Holiday!")
    activity = input("Do you prefer hiking or cycling? ").lower()

    if activity == "hiking":
        print("Your activity plan: Explore nature trails and go hiking!")
    elif activity == "cycling":
        print("Your activity plan: Enjoy an exciting cycling trip!")
    else:
        print("Your activity plan: Try an exciting outdoor adventure!")

elif choice == "relaxation" or choice == "3":
    print("You have chosen a Relaxation Holiday!")
    activity = input("Do you prefer reading or spa treatment? ").lower()

    if activity == "reading":
        print("Your activity plan: Spend the day reading and relaxing!")
    elif activity == "spa treatment":
        print("Your activity plan: Enjoy a refreshing spa treatment!")
    else:
        print("Your activity plan: Enjoy a peaceful and relaxing day!")

else:
    print("Invalid choice! Please select Beach, Adventure, or Relaxation.")

print("Thank you for using the Holiday Activity Planner!")
