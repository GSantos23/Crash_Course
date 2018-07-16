# Exercise 8.8
'''
Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
'''
def make_album(artist, album, tracks=''):
	"""Display music album info
	artist -> string
	album  -> string
	tracks -> number"""
	music = {'artist':artist, 'album':album}
	if tracks:
		music['tracks'] = tracks

	return music


while True:
	print("\nType your music knowledge.\nType 'q' to quit")

	artist_name = input("Artist: ")
	if artist_name == 'q':
		break

	album_name = input("Album: ")
	if album_name == 'q':
		break

	information = make_album(artist_name, album_name)
	print(information)