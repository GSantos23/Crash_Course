# Sample 15.2
import matplotlib.pyplot as plt 

#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
	edgecolors='none', s=40)


# Set chart and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
plt.axis([0, 1100, 0, 1100000])

# Use this to maximized window
#figManager = plt.get_current_fig_manager()
#figManager.window.showMaximized()

# To only save use savefig
# To save and display, please uncomment lines 25 - 26, 32 - 33

figure = plt.gcf()
#plt.show()
#plt.draw()
# To save images
figure.savefig('squares_plot4.png', bbox_inches='tight')




