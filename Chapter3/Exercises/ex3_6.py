# Exercise 3.6
# More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
#
#	• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
#	statement to the end of your program informing people that you found a
#	bigger dinner table.
#	• Use insert() to add one new guest to the beginning of your list.
#	• Use insert() to add one new guest to the middle of your list.
#	• Use append() to add one new guest to the end of your list.
#	• Print a new set of invitation messages, one for each person in your list.

dinner = ['Abraham Lincon', 'Linus Torvalds', 'Robert Tomasulo']

print(dinner[0])
print(dinner[1])
print(dinner[2])

print("The guest who can't make it is: " + dinner[2])
print()

dinner.remove('Robert Tomasulo')
#print(dinner)
dinner.append('Stephen King')
#print(dinner)

message = ", you are invited to the big dinner party"

print(dinner[0] + message)
print(dinner[1] + message)
print(dinner[2] + message)

print("\n\nHey everyone, I found a bigger table. :)")

dinner.insert(0,'Elon Musk')
dinner.insert(2,'Bill Gates')
dinner.append('Nikola Tesla')
#print(dinner)

message2 = ", you are invited to the new party"

print(dinner[0] + message2)
print(dinner[1] + message2)
print(dinner[2] + message2)
print(dinner[3] + message2)
print(dinner[4] + message2)
print(dinner[5] + message2)



