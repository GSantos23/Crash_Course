players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])
print(players[1:4])
print(players[:4])			# To start from begining of list
print(players[2:])			# To print until last member
print(players[-3:])			# From the end

print("Here are the first three players on my team: ")
for player in players[:3]:
	print(player.title())