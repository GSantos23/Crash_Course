# Exercise 16.5
'''
All Countries: On the population maps we made in this section, our pro-
gram couldn’t automatically find two-letter codes for about 12 countries. Work
out which countries are missing codes, and look through the COUNTRIES diction-
ary for the codes. Add an if - elif block to get_country_code() so it returns the
correct country code values for these specific countries:
----------------------------------------------------------
if country_name == 'Yemen, Rep.'
return 'ye'
elif --snip--
----------------------------------------------------------
Place this code after the COUNTRIES loop but before the return None state-
ment. When you’re finished, you should see a more complete map.
'''
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
	"""Return the Pygal 2-digit country code for the given country"""
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code

	if country_name == 'Yemen, Rep.':
		return 'ye'
	elif country_name == 'Bolivia':
		return 'bo'
	elif country_name == 'Venezuela, RB':
		return 've'
	elif country_name == 'Vietnam':
		return 'vn'
	elif country_name == 'Iran, Islamic Rep.':
		return 'ir'
	elif country_name == 'Egypt, Arab Rep.':
		return 'eg'
	elif country_name ==  'Libya':
		return 'ly'
	elif country_name == 'Congo, Dem. Rep.':
		return 'cd'
	elif country_name == 'Congo, Rep.':
		return 'cg'
	elif country_name == 'Korea, Dem. Rep.':
		return 'kp'
	elif country_name == 'Korea, Rep.':
		return 'kr'
	elif country_name == 'Tanzania':
		return 'tz'
	elif country_name == 'Lao PDR':
		return 'la'
	elif country_name == 'Hong Kong SAR, China':
		return 'hk'
	elif country_name == 'Macedonia, FYR':
		return 'mk'
	elif country_name == 'Slovak Republic':
		return 'sk'
	elif country_name == 'Macao SAR, China':
		return 'mo'
	elif country_name == 'Sub-Saharan Africa (developing only)':
		return 'eh'
	elif country_name == 'Kyrgyz Republic':
		return 'kg'


	# If the country wasn't found, return none
	return None

#print(get_country_code('Andorra'))
#print(get_country_code('United Arab Emirates'))
#print(get_country_code('Afghanistan'))