# Exercise 3.5
# Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
#	• Start with your program from Exercise 3-4. Add a print statement at the
#	end of your program stating the name of the guest who can’t make it.
#	• Modify your list, replacing the name of the guest who can’t make it with
#	the name of the new person you are inviting.
#	• Print a second set of invitation messages, one for each person who is still
#	in your list.

dinner = ['Abraham Lincon', 'Linus Torvalds', 'Robert Tomasulo']

print(dinner[0])
print(dinner[1])
print(dinner[2])

print("The guest whi can't make it is: " + dinner[2])

dinner.remove('Robert Tomasulo')
#print(dinner)
dinner.append('Stephen King')
#print(dinner)

message = ", you are invited to the big dinner party"

print(dinner[0] + message)
print(dinner[1] + message)
print(dinner[2] + message)
