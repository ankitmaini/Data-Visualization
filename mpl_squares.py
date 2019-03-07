import matplotlib.pyplot as plt

plt.scatter(2,4, s = 200, color = 'green',  marker = 's')

plt.title('Square Numbers', fontsize = 24, color = 'red')
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square', fontsize = 14)

plt.tick_params(axis='both', which ='major', labelsize = 5)

plt.show()