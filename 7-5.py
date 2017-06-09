
message = "Please enter your age under here: "
age = int(input(message))
	
if  age < 3:
	print("Your tickets is free")
elif 3 <= age <= 12:
	print("You tickets need 10 dollars")
elif age > 12:
	print("You tickest need 15 dollars")

