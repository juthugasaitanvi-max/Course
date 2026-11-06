# Loop:A loop lets you repeat a block of code without writing it again and again .
# Types of loop:-
# For loop:It repeats a code over a sequence.
# While loop:It lets us repeat a code as long as the condition is true.
# Nested loop:It lets us repeat a code by placing 1 loop inside another while or for loop.
# Ex for "for loop":
# a="mandarin"
# for x in range(1,10,2) :  #(for x in x<a.length, x++) range(start,stop,step) range(stop)
#     print(x)

# # a
# # p
# # p
# # l
# # e


# Activity 1:
# 1) Ask the user to enter a number and store it in `n`.

# 2) Set `sum` to 0.
#    (This will store the running total.)

# 3) Use a `for` loop from 1 to `n` (inclusive):
#    - In each step, add the current value of `i` to `sum`.

# 4) After adding, print the current value of `sum`.
#    (So the user can see how the sum increases step by step.)

# n=int(input("Choose a number "))
# sum=0
# for x in range(1,n+1):
#     sum=sum+x
#     print(sum)

# Activity 2:
# 1) Ask the user to enter a word or sentence and store it in `string`.

# 2) Create an empty string called `string2`.
#    (This will store the reversed version.)

# 3) Loop through each character `i` in `string`:
#    - Add the character `i` in front of `string2`
#    - This builds the reversed string step by step.

# 4) Print the original string (`string`).

# 5) Print the reversed string (`string2`).

string=input("Enter your string ")
string2=""
for t in string:
    string2=t+string2
print("Original string",string)
print("Reverse string",string2) 

# Activity 3:
# 1) Ask the user to enter a number (greater than 1) and store it in `n`.

# 2) Print a message saying you will display numbers from `n` down to 1.

# 3) Use a `for` loop that starts from `n`, goes down to 1, and decreases by 1 each time.

# 4) Inside the loop, print the current value of `i` (so numbers appear in reverse order).