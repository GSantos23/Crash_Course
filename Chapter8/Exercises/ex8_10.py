# Exercise 8.10
'''
Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by 
adding the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.
'''

def  show_magicians(magic_names):
    """Displays magicians names"""
    print("Magic Show presents:\n")
    while magic_names:
        old_name = magic_names.pop()
        print(old_name.title())
        super_names.append(old_name)
        

def make_great(super_names):
    """Adds great to the name"""
    print("\nPerforming as: ")
    for new_name in super_names:
        print("The Great " + new_name.title()) 
        
    

# List
magic_names = ['henry', 'paul', 'michael']
super_names = []

show_magicians(magic_names)
make_great(super_names)


