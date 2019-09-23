first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
operation = input("Choose the operation (+, -, /, *): ")

if first_number.isdigit() and second_number.isdigit():
	first_number = int(first_number)
	second_number = int(second_number)

	if operation == "+":
		answer = first_number + second_number
		print("The answer is: %s" % answer)
	elif operation == "-":
		answer = first_number - second_number
		print("The answer is: %s" % answer)
	elif operation == "/":
		answer = first_number / second_number
		print("The answer is: %s" % answer)	
	elif operation == "*":
		answer = first_number * second_number
		print("The answer is: %s" % answer)
	else:
		print("Invalid operation. Try again please.")
else:
	print("Invalid numbers. Try again please.")