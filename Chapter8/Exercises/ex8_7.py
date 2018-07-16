# #xercise 8.7
'''
Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing 
different albums. Print each return value to show that the dictionaries are
storing the album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the num-
ber of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.
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


album_1 = make_album('Metallica', 'HardWired')
print(album_1)

album_2 = make_album('Pink Floyd', 'Dark Side of the Moon')
print(album_2)

album_3 = make_album('Linkin Park', 'Meteora')
print(album_3)

album_4 = make_album('Nirvana', 'Nevermind', tracks = 12)
print(album_4)