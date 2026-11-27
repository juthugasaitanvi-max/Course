# Build a game where the computer picks a secret number between 1 and 50. You have 5 attempts to guess it. After every wrong guess your program shows a hint telling you how close you are. Remaining lives are shown as hearts after each attempt.

 

# 💡 Hint: Store your secret number in a variable — for example: secret = 27

 

# If you already know the random module, feel free to use it! This test checks your logic (conditions, loops, input/output).

 

# What you need to use

# 1. int(input()) → read the player’s guess

# 2. while loop → stops after 5 attempts or when player wins

# 3. if/elif/else → hint system: 🧊 ice cold, 🥶 cold, 🌡️ warm, or 🔥 hot

# 4. for loop → shows remaining ❤️ hearts after each wrong guess

# 5. win/loss message → reveals the secret number if attempts run out

 

# What you’ll be marked on

# Program runs without any errors → 5 marks

# int(input()) used to read the player’s guess → 5 marks

# while loop stops after 5 attempts or on correct guess → 10 marks

# Hint system prints ice cold / cold / warm / hot → 10 marks

# for loop shows correct hearts after each wrong guess → 5 marks

# Win message shown / secret revealed if attempts run out → 5 marks

 

# Total → 40 marks 🏆

 

# How to submit 🚀

# Push your completed code to a public GitHub repository and paste the repo link in the box below. Make sure your repo is public and your code runs correctly before submitting.


player_number=int(input("Guess a number from 1 to 50"))
total_hearts=5
secret=25

while total_hearts False:
    print("You lose")

if player_number >secret:
    print("Ice cold!")
elif player_number <secret:
    print("Cold!")
elif player_number  >secret:
    print("Warm")
else:
    print("Hot")

wrong_ans=total_hearts-1

for wrong_ans in range(1,5):
    print("Wrong , 4 hearts left ")
for wrong_ans in range(1,4):
    print("Wrong, 3 hearts left")