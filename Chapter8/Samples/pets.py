# Sample 8.2
def describe_pet(animal_type, pet_name):
	"""Display information about a pet"""
	print("\nI have aa " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie') 
describe_pet(pet_name='harry', animal_type='hamster')	# keyboard argument