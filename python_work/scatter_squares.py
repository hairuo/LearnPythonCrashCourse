import matplotlib.pyplot as plt

#~ x_values = [1, 2, 3, 4, 5]
#~ y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

#~ plt.scatter(x_values, y_values, s=400)
#~ plt.scatter(x_values, y_values, c='red', edgecolor='none', s=400)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
	edgecolor='none', s=40)

# Set chart title and label axies.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

# Set the range for each axis.
#~ plt.axis([0, 1100, 0, 1100000])

#~ plt.show()
plt.savefig('squares_plot.png', box_inches='tight')


