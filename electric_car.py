from car import Car
			
class Battery():
	"""A simple attempt to model a battery for an electric car."""
	
	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size
		
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + " -kwh battery.")
	
				
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		super().__init__(make, model, year)
		#~ self.battery_size = 70
		self.battery = Battery()
		
	def describe_battery(self):
		"""Print a statement describing the batery size"""
		print("This car has a " + str(self.battery_size) + " -kwh battery.")
		
	def fill_gas_tank():
		"""Electric cars don't have gas tanks."""
		print("This car doesn't need a gas tank!")
		
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
#~ my_tesla.describe_battery()
my_tesla.battery.describe_battery()
