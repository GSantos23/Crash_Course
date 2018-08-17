# Exercise 15.1
# Cubes: A number raised to the third power is a cube. Plot the first five
# cubic numbers, and then the first 5000 cubic numbers
import matplotlib.pyplot as plt


#x_values = list(range(1,6))
x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values)
plt.title("Cubic Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
#plt.tick_params(axis='both', which='major', labelsize=14)

# Use this to maximized window
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

plt.show()