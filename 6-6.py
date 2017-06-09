favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	'jack': 'c',
	}
	
investigated_people = ['jen', 'jack']

for name in favorite_languages.keys():
	print("Hi " + name.title())
	if name in investigated_people:
		print("Thanks for your investigation!\n")
	else:
		print("Would you take part in our investigation?\n")
	
