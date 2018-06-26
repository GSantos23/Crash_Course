dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])

# Generare an error
#dimensions[0] = 250
print("Original dimensions: ")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
	print(dimension)