from datetime import datetime, date

def check_birthdate(year, month, day): 
	today = datetime.now()
	birthdate = datetime(year, month, day)
	if birthdate > today:
		return False
	else:
		return True

def calculate_age(year,month,day):
	today = datetime.now()
	birthdate = datetime(year, month, day)

	age = today - birthdate
	print("You are %s years old" % (age.days / 365))

year = int(input("Enter year of birth: "))
month = int(input("Enter month of birth: "))
day = int(input("Enter day of birth: "))

if check_birthdate(year, month, day)==True:
	calculate_age(year, month, day)
else:
	print("invalid birthdate.")
# 	import datetime
# 	x = datetime.datetime.now()
