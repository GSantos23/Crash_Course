# Exercise 5.2
"""
More Conditional Tests: You don’t have to limit the number of tests you
create to 10. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
	• Tests for equality and inequality with strings
	• Tests using the lower() function
	• Numerical tests involving equality and inequality, greater than and
	less than, greater than or equal to, and less than or equal to
	• Tests using the and keyword and the or keyword
	• Test whether an item is in a list
	• Test whether an item is not in a list
"""

# Equality and iniquality with strings
car = 'Volkswagen'
print("Is car == 'Volkswagen'? I predict True.")
print(car == 'Volkswagen')

print("\nIs car == 'Honda'? I predict False")
print(car == 'Honda')

# Using lower() function
print ("\nLower function: ",car == car.lower())


# Numeical test
num1, num2, num3 = 10, 15, 20

print("\nnum1 == num2: ", num1 == num2)
print("\nnum1 != num2: ", num1 != num2)
print("\nnum1 > num2: ", num1 > num2)
print("\nnum1 < num2: ", num1 < num2)
print("\nnum1 >= num2: ", num1 >= num2)
print("\nnum1 <= num2: ", num1 <= num2)

# and, or
print("\nnum1 or num2 >  num3: ", (num1 or num2) > num3)
print("\nnum1 and num2 <  num3: ", (num1 and num2) < num3)

# Lists
print()
computers = ['Dell', 'HP', 'Asus']
brand = 'Lenovo'

if brand not in computers:
	print(brand + ", is not on the list")

brand = 'Asus'

if brand not in computers:
	print(brand + ", is not on the list")
else:
	print("\n" + brand + ", is on the list")