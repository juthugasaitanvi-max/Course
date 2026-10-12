team1 = int(input("Enter Team 1 points: "))
team2 = int(input("Enter Team 2 points: "))

total = team1 + team2
average = total / 2

print("\nClassroom Points Calculator")
print("Team1 Points:",team1)
print("Team2 Points:",team2)
print("Total Points:", total)
print("Average Points:", average)

stars1 = team1 // 10
stars2 = team2 // 10

print("Team1 Reward Stars:", stars1)
print("Team2 Reward Stars:", stars2)

if team1 > team2:
    print("Team 1 scored more points!")
elif team2 > team1:
    print("Team 2 scored more points!")
else:
    print("Both teams scored equally!")

team1 += 5
team2 += 5

print("Updated Team 1 Points:", team1)
print("Updated Team 2 Points:", team2)

