# Exercise 4.12
"""
More Loops: All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('canoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
for mine in my_foods:
	print(mine)


print("\nMy friend's favorite foods are:")
for friends in friend_foods:
	print(friends)
