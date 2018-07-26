# Importing Multiple Classes from a Module
'''
from electric_car import Car, ElectricCar

my_beetle = Car('Volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
'''

# Importing an Entire Module
import  electric_car

my_beetle = electric_car.Car('Volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = electric_car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())