my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# This doesn't work
#friend_foods = my_foods

my_foods.append('canoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)


print("\nMy frind's favorite foods are:")
print(friend_foods)