# Sample 8.8
def buil_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user"""
	profile = {}
	profile['first_name'] = first
	profile['last_name']  = last
	for key, value in user_info.items():
		profile[key] = value
	return profile


user_profile = buil_profile('albert', 'einstein',
							location = 'princeton',
							field = 'physics')

print(user_profile)