skills = ["swim", "run", "cycle", "weightlift", "boxing", "golf"]
cv = {}

name = input("What's your name? ")
cv["name"] = name

# cv["name"] = input("What's your name?")

age = int(input("How old are you? "))
cv["age"] = age

experience = int(input("How many years of experience do you have? "))
cv["experience"] = experience

cv["skills"] = []

print("Skills:")
for idx, x in enumerate(skills):
	print("%s- %s" %(idx+1, x))

skill1 = int(input("Choose a skill from above by entering its number: "))
cv["skills"].append(skills[skill1 - 1])

skill2 = int(input("Choose another skill from above by entering its number: "))
cv["skills"].append(skills[skill2 - 1])

if (age > 22) and (experience >= 3) and (skills[0] in cv["skills"]) :
	print("You have been accepted, %s" % name)
else:
	print("Sorry to inform you we cannot have you on board, %s" % name)

