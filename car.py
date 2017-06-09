"""A class that can be used to represent a car."""

class Car():
		"""A simple attempt to represent a car."""
		
		def __init__(self, make, model, year):
			"""Initialize attributes to describe a car"""
			self.make = make
			self.model = model
			self.year = year
			self.odometer_reading = 20
			
		def get_descriptive_name(self):
			"""Return a neatly formatted descriptive name."""
			long_name = str(self.year) + ' ' + self.make + ' ' + self.model
			return long_name.title()
			
		def read_odometer(self):
			"""Print a statement showing the car's mileage."""
			print("This car has " + str(self.odometer_reading) + 
			" miles on it.")
			
		def update_odometer(self, mileage):
			"""Set the odometer reading to the given value.
			Reject the change if it attempts to roll the odometer back.
			"""
			if mileage >= self.odometer_reading:
				self.odometer_reading = mileage
			else:
				print("You can't roll back an odometer!")
				
		def increment_odometer(self, miles):
			"""Add the given amount to the odometer reading."""
			self.odometer_reading += miles
			
			
class Battery():
	"""A simple attempt to model for an electric car."""
	
	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size
		
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + " -kwh battery.")
		
	def get_range(self):
		"""Print a statement about the range thhis battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
			
		message = "This car can go approximately " + str(range)
		message += " miles on a full change."
		print(message)
		

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		super().__init__(make, model, year)
		#~ self.battery_size = 70
		self.battery = Battery()

