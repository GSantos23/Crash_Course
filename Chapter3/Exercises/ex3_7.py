# Exercise 3.7
# Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
#		• Start with your program from Exercise 3-6. Add a new line that prints a
#		message saying that you can invite only two people for dinner.
#		• Use pop() to remove guests from your list one at a time until only two
#		names remain in your list. Each time you pop a name from your list, print
#		a message to that person letting them know you’re sorry you can’t invite
#		them to dinner.
#		• Print a message to each of the two people still on your list, letting them
#		know they’re still invited.
#		• Use del to remove the last two names from your list, so you have an empty
#		list. Print your list to make sure you actually have an empty list at the end
#		of your program.

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

print("Hi, sorry for bother you. I only have sace for two people :(")

#dinner.pop()
print("Sorry " + dinner.pop() + ". Next time for sure")
print("Sorry " + dinner.pop() + ". Next time for sure")
print("Sorry " + dinner.pop() + ". Next time for sure")
print("Sorry " + dinner.pop() + ". Next time for sure")
#print(dinner)

print(dinner[0] + " and " + dinner[-1] + " are still invited.")

# Now to remove everyone
dinner.remove('Abraham Lincon')
dinner.remove('Elon Musk')
print(dinner)