#~ cars = ['bmw', 'audi', 'toyota', 'subaru']
#~ cars.sort(reverse=True)
#~ print(cars)

#~ print("Here is the original list:")
#~ print(cars)

#~ print("\nHere is the sorted list:")
#~ print(sorted(cars))

#~ print("\nHere is the original list again:")
#~ print(cars)

#~ cars.reverse()
#~ print(cars)
#~ print(len(cars))

#~ motorcycles = ['honda', 'yamaha', 'suzuki']
#~ print(motorcycles[-1])

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
