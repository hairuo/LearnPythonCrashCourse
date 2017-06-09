def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
			words = contents.split()
			num_words = len(words)
			print("The file " + filename + " has about " + str(num_words) + " words.")
	except FileNotFoundError:
		#~ msg = "Sorry, the file " + filename + " does not exist."
		#~ print(msg)
		pass	# Failing Silently
#~ filename = 'alice.txt'
#~ count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)
