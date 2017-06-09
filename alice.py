
filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)
#~ else:
	#~ #calculate how many words in this file
	#~ words = contents.split()
	#~ num_words = len(words)
	#~ print("The file " + filename + " has about " + str(num_words) + " words.")
	
