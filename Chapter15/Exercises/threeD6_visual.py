# Exersice 15.8
'''
Three Dice: If you roll three D6 dice, the smallest number you can roll is 3
and the largest number is 18. Create a visualization that shows what happens
when you roll three D6 dice.
'''

import pygal

from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list 
results = [die_1.roll() + die_2.roll() + die_3.roll() 
for roll_num in range(1000)]

# Analize the results
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result+1)]

# Visualize the results
hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times"
#hist.x_labels  = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 
#'13', '14', '15', '16']
hist.x_labels = [str(x) for x in range(3,max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('die_visual.svg')