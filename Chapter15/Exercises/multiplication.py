# Exercise 15.9
'''
Multiplication: When you roll two dice, you usually add the two numbers
together to get the result. Create a visualization that shows what happens 
if you multiply these numbers instead.
'''
import pygal

from die import Die

die_1 = Die()
die_2 = Die()


# Make some rolls, and store results in a list 
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

# Analize the results
max_result = die_1.num_sides * die_2.num_sides 
frequencies = [results.count(value) for value in range(3, max_result+1)]

# Visualize the results
hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = [str(x) for x in range(1,max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('die_visual.svg')