#coding: utf-8
#~ motorcycles = ['honda', 'yamaha', 'suzuki']
#~ print(motorcycles)

#~ motorcycles[0] = 'ducati'
#~ print(motorcycles)

#~ motorcycles.append('ducati')
#~ print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

#~ print(motorcycles)

motorcycles.insert(0,'ducati')
#~ print(motorcycles)

#~ del motorcycles[1]
#~ print(motorcycles)
#~ print(motorcycles)
#~ popped_motorcycle = motorcycles.pop()
#~ print(motorcycles)
#~ print(popped_motorcycle)
#~ last_owned = motorcycles.pop()
#~ print("The last motorcycle I owned was a "+last_owned.title()+".")
#~ first_owned = motorcycles.pop(0)
#~ print("The first motorcycle I owned was a "+first_owned.title()+".")
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA '+too_expensive.title()+'is too expensive for me.')

# 以上，学习使用了.append(),.insert(), .pop(), .remove(), del(注意不是delete)等等。
















