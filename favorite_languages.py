#~ favorite_languages = {
	#~ 'jen': ['python', 'ruby'],
	#~ 'sarah': 'c',
	#~ 'edward': ['ruby', 'go'],
	#~ 'phil': ['python', 'haskell'],
	#~ 'Jack': 'c',
	#~ }
#~ for name, languages in favorite_languages.items():
	#~ print("\n" + name.title() + "'s favorite languages are:")
	#~ for language in languages:
		#~ print("\t" + language.title())	
	
########################################	
 	
#~ print("Sarah's favorite language is " +  
	#~ favorite_languages['sarah'].title() +
	#~ ".")
#~ for name, language in favorite_languages.items():
	#~ print(name.title() + "'s favorite language a " +
		#~ language.title() + ".")
#~ for name in favorite_languages.keys():
	#~ print(name.title())
#~ friends = ['phil', 'sarah']
#~ for name in favorite_languages.keys():
	#~ print(name.title())
	
	#~ if name in friends:
		#~ print(" Hi " + name.title() +
			#~ ", Isee your favorite language is " +
			#~ favorite_languages[name].title() + "!")
	#~ if 'erin' not in favorite_languages.keys():
		#~ print("Erin, please take our poll!")
#~ for name in sorted(favorite_languages.keys()):
	#~ print(name.title() + ", thank you for taking the poll.")
#~ print("The following languages have been mentioned:")
#~ for language in set(favorite_languages.values()):
	#~ print(language.title())

#######################################


from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phi'] = 'python'

for name, language in favorite_languages.items():
	print(name.title() + "s favorite language is " + 
		language.title() + ".")

