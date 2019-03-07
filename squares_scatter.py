import matplotlib.pyplot as plt

x_vals = list(range(1, 1001, 20))
y_vals = [x**2 for x in x_vals]


plt.scatter(x_vals, y_vals, s = 4 , c =x_vals, edgecolor = 'none', cmap=plt.cm.Blues)

# Setting the range for each axis
plt.axis([0,1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches = 'tight')
plt.show()