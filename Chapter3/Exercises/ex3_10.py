# Exercise 3.10
# Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or any-
# thing else you’d like. Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.

names = ['Gerson', 'Abigail', 'Elizabeth', 'Harmen', 'Yose']

print(str(len(names)))

names.append('Chris')
print(names)

names.insert(0, 'Michael')
print(names)

del names[0]
print(names)

names.remove('Harmen')
print(names)

names.sort()
print(names)

names.sort(reverse=True)
print(names)