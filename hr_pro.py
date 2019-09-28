print("Welcome to HR Pro 2019")
# print("""
# 	Options:
# 	1. Show Employees
# 	2. Show Manager
# 	3. Add An Employee
# 	4. Add A Manager
# 	5. Exit
# 	""")

from datetime import date

# today = date.today()
# print("Today's date:", today.year)

class Employee:
	def __init__(self, name, age, salary, employment_year):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_year = employment_year

	def get_working_years(self):
		return date.today().year - int(self.employment_year)

	def __str__(self):
		return "Name: %s, Age: %s, Salary: %s, Working Years: %s" % (self.name, self.age, self.salary, self.get_working_years())

class Manager(Employee):
	def __init__(self, name, age, salary, employment_year, bonus_percentage):
		super().__init__(name, age, salary, employment_year)
		self.bonus_percentage = bonus_percentage

	def get_bonus(self):
		return float(self.bonus_percentage) * float(self.salary)

	def __str__(self):
		return "Name: %s, Age: %s, Salary: %s, Working Years: %s, Bonus: %s" % (self.name, self.age, self.salary, self.get_working_years(), self.get_bonus())

employees = []
managers = []

print("""
	Options:
	1. Show Employees
	2. Show Manager
	3. Add An Employee
	4. Add A Manager
	5. Exit
	""")

option = int(input("What would you like to do? "))

while option != 5:
	if option == 1: 
		for employee in employees:
			print(employee)
	elif option == 2:
		for manager in managers:
			print(manager)
	elif option == 3:
		name = input("Name: ")
		age = input("Age: ")
		salary = input("Salary: ")
		employement_year = input("Employment year: ")
		employee = Employee(name, age, salary, employement_year)
		employees.append(employee)
	elif option == 4:
		name = input("Name: ")
		age = input("Age: ")
		salary = input("Salary: ")
		employment_year = input("Employment year: ")
		bonus_percentage = input("Bonus Percentage: ")
		manager = Manager(name, age, salary, employment_year, bonus_percentage)
		managers.append(manager)
	print("""
	Options:
	1. Show Employees
	2. Show Manager
	3. Add An Employee
	4. Add A Manager
	5. Exit
	""")
	option = int(input("What would you like to do? "))
