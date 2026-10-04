name = "Saitanvi"
age = 12
club = "Science"
badge_code = "SC12345"

print(type(name))
print(type(age))
print(type(club))
print(type(badge_code))

age = str(age)

short_code = badge_code[:4]

badge = "Name: " + name + " | Age: " + age + " | Club: " + club + " | Code: " + short_code

print(badge)