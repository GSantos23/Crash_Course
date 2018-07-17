# Exercise 8.9
'''
Magicians: Make a list of magician’s names. Pass the list to a function
called show_magicians() , which prints the name of each magician in the list
'''

def  show_magicians(names):
    """Displays magicians names"""
    for id in names:
        print("Welcome, " + id.title())
        
        
# List
magic_names = ['henry', 'paul', 'michael']

show_magicians(magic_names)

        
        