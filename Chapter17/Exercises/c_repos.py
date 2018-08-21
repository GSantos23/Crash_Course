# Exercise 17.1
'''
Other Languages: Modify the API call in python_repos.py so it generates
a chart showing the most popular projects in other languages. Try languages
such as JavaScript, Ruby, C, Java, Perl, Haskell, and Go.
'''
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:c&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)

# Store API response in a variable
response_dict = r.json()

# Process results
print(response_dict.keys())

print("Total repositories: ", response_dict['total_count'])

# Explore information about the repositories
repo_dicts = response_dict['items']
print("Number of items: ", len(repo_dicts))

# Examine available keys
'''
repo_key = repo_dicts[0]

print("\nKeys: ", len(repo_key))
for key in sorted(repo_key.keys()):
	print(key)
'''

names, plot_dicts = [], []

for repo_dict in repo_dicts:
	names.append(repo_dict['name'])

	# Get the project description if one is available
	description = repo_dict['description']
	if not description:
		description = "No description provided"

	plot_dict = {
		'value': repo_dict['stargazers_count'],
		'label': description,
		'xlink': repo_dict['html_url'],
		}
	
	plot_dicts.append(plot_dict)

# Make visualization
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred C Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('c_repos.svg')