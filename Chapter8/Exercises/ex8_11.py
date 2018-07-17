# Exercise 8.11
'''
Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate
 list.
Call show_magicians() with each list to show that you have one list of the 
original names and one list with the Great added to each magician’s name.
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

show_magicians(magic_names[:])
make_great(super_names)
