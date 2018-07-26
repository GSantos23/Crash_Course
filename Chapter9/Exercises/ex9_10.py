# Exercise 9.10
'''
Imported Restaurant: Using your latest Restaurant class, store it in a mod-
ule. Make a separate file that imports Restaurant . Make a Restaurant instance,
and call one of Restaurant ’s methods to show that the import statement is work-
ing properly.
'''
from restaurant import Restaurant

my_restaurant = Restaurant('Los Arcos', 'Sea Food')
my_restaurant.describe_restaurant()