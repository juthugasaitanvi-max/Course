#If-elif-else statement:It is used when python wants us to choose more than 2 outcomes.
#Example:
# Marks=100
# if Marks>=90:
#     print("Grade A:)")
# elif Marks>=70:
#     print("Grade B:|")
# elif Marks>=50:
#     print("Grade C:/")
# else:
#     print("Fail!:(") 

# AND operator:It always combines 2 conditions together.Both conditions must be true for the whole expression to be true.
#Example:
# Age=10
# Has_license=True
# if Age>=18 and Has_license:
#     print("You are eligible to drive")
# else:
#     print("You are not eligible to drive")

# OR operator:Atleast 1 condition must be true for the result to be true.
# Example:
# Day="Sunday"
# if Day=="Saturday" or Day=="Sunday":
#     print("It's literally weekend")
# else:
#     print("It's literally a week day")

# NOT operator:It reverses a condition , true statements become false and false statements become true. 
# Example:
# Is_Raining=False
# if not Is_Raining:
#     print("You can go out for a walk")
# else:
#     print("Stay at home")

# Example for all logical operators combined:
Age=15
is_student=True
if (Age<18 or Age>50)and is_student:
    print("You get a discount!")
else:
    print("You don't get a discount!")

# STEPS

# Step 1: Print the welcome message: " === Smart School Day Planner === ".

# Step 2: Use input() to ask for the day, weather, and homework status. Store each in a variable.

# Step 3: Print the plan header using the day variable in an f-string.

# Step 4: Write if-elif-else to classify the day type (weekend / Monday / Friday / other school day).

# Step 5: Write an if statement using AND to check sunny weather and homework done together.

# Step 6: Write an if statement using OR to check rainy or cloudy weather.

# Step 7: Write an if statement using NOT to catch when homework is not done.

# Step 8: Write if-elif-else using AND, OR, and NOT combined to print the best plan message.

# Step 9: Print the closing message: "Plan complete! Have a wonderful day!"

# Step 10: Run the program with three different combinations of inputs to test all branches.


