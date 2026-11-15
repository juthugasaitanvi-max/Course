
# Homework Completion Tracker

total_tasks = 5
completed_tasks = 0

print("Welcome to my Homework Completion Tracker!")

while completed_tasks < total_tasks:
    print("\nHomework Progress:")
    print("Completed tasks:", completed_tasks)
    print("Remaining tasks:", total_tasks - completed_tasks)

    answer = input("Have you completed a homework? (yes/no): ").lower()

    if answer == "yes":
        completed_tasks += 1
        print("Great! Homework  completed.")
    elif answer == "no":
        print("Keep working! You can do it.!")
    else:
        print("Invalid input. Please enter yes or no.")

print("\nCongratulations!")
print("All homework  are completed!")
print("You have finished your homework tracker!.")
