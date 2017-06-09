class Restaurant():
	""" creat a class of Restaurant"""
	
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print("This restaurant is called " 
				+ self.restaurant_name.upper()
				+ ".")
		print("The type of this restaurant is " 
				+ self.cuisine_type.title() 
				+ ".")
		
	def open_restaurant(self):
		print("Our restaurant is openning.")
		
KFC = Restaurant('kfc', 'fast food')
KFC.describe_restaurant()
KFC.open_restaurant()
		
