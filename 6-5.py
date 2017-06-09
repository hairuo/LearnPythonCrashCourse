
rivers = {
	'Yangzijiang': 'china', 
	'nile': 'egypt', 
	'amazon': 'southamerica',
	}
for river in rivers.keys():
	print("The " + river.title() + 
	" runs through " + 
	rivers[river].title()+
	".")
 
