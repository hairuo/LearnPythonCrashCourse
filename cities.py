
prompt = "\nPlease enter the name of a city you have visited:\n "
prompt += "\nEnter 'quit' when you are finished. "



while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")
