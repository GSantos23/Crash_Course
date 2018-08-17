# Exercise 15.3
'''
Molecular Motion: Modify rw_visual.py by replacing plt.scatter() with
plt.plot() . To simulate the path of a pollen grain on the surface of a 
drop of water, pass in the rw.x_values and rw.y_values , and include a 
linewidth argument. Use 5000 instead of 50,000 points.
'''
import matplotlib.pyplot as plt 

from random_walk import RandomWalk

while True:
	# Make a random walk, and plot the points
	rw = RandomWalk(5000)
	rw.fill_walk()

	# Set the size of the plotting window
	#plt.figure(figsize=(10,6))
	plt.figure(dpi=128, figsize=(10,6))

	point_numbers = list(range(rw.num_points))
	plt.plot(rw.x_values, rw.y_values, linewidth=2)

	# Emphasize the first and last points
	# marker argument to plot the start and end point with a circle
	plt.plot(0,0, color='green', marker='o', linewidth=2)
	plt.plot(rw.x_values[-1], rw.y_values[-1], color='red', marker='o'
		, linewidth=2)


	# Remove the axes
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break