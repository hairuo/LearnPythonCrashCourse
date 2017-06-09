#~ def get_formatted_name(first, last):
	#~ """Generate a neatly formatted full name."""
	#~ full_name = first + ' ' + last
	#~ return full_name.title()
	
################	

#~ def get_formatted_name(first, middle, last):
	#~ """Generate a neatly formatted full name."""
	#~ full_name = first + ' ' + middle + ' ' + last
	#~ return full_name.title()

#########################

def get_formatted_name(first, last, middle=''):
	"""Generate a neatly formatted full name."""
	if middle:
		full_name = first + ' ' + middle + ' ' + last
	else:
		full_name = first + ' ' + last
	return full_name.title()
