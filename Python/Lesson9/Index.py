# While loop:It will be running until the condition is true.When the the condition becomes false , the loop stops.
# Example:
# age=1
# while age <=5:
#     print("age is",age)
#     age=age+1

# When to use while loop: Use a while loop when you don't know in advance how many times something needs to be repeated but u know when it should stop.
# Ex : You are entering a password , u will be entering the password until it is correct.
# What causes an infinite loop:An infinite loop is a loop that never stops ,it keeps running forever.
# Example:
# age=1 
# while age <=3:
#     print("Age is",age)
    


# Chore Checklist Countdown
# A Chore Checklist Countdown that asks about each chore one at a time, uses a while loop to keep checking until the entire list is empty, and prints a final summary of every chore completed today.

#Step 1: Set total_chores to 4, store it as original_count, and print how many chores are on today's list.

# Step 2: Set up a completed_count counter starting at 0 and a chore_num counter starting at 1.

# Step 3: Start a while loop that keeps running as long as chore_num is less than or equal to total_chores.

# Step 4: Inside the loop, work out the current chore's name from chore_num, then ask if it has been finished.

# Step 5: If the answer is yes, increase completed_count and chore_num by 1; otherwise, print a message and let the loop ask about the same chore again.

# Step 6: Once the while loop ends, print the completion message, then safely demonstrate an infinite loop's

# condition, using a break to stop it after 3 rounds.

# Step 7: Print the final chore checklist summary showing chores assigned, completed, and remaining.


total_chores=4
original_count=total_chores 
print("total no. of chores for today ",original_count)

completed_count=0
chore_num=1
while chore_num <=total_chores:
    if chore_num ==1:next_chore="Cleaning"
    elif chore_num==2:next_chore="Mopping"
    elif chore_num==3:next_chore="Washing the dishes"
    else:next_chore="Ironing"
    answer=input(f"have u finished {next_chore}? YES/NO: ")
    if answer=="YES":
        completed_count+=1
        chore_num+=1
        print("Great job! :)")
    else:
        print("Finish it and check again! :( ")
    print("Chores remaining",total_chores-completed_count)
print("Yay,all chores completed! :)")