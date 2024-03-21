# We have a list what are called, "varibles."
# The character = (equals) purpose is to give data (numbers, strings, etc.) names (i.e. cars_driven, passengers, etc.)

# The amount of cars available
cars = 100

# The space inside the car i.e. the amount of persons that can fit inside the car
space_in_a_car = 4.0

# The amount of drivers available to drive (1 driver per vehicle)
drivers = 30

# Total amount of passengers 
passengers = 90



# Underscore characters (_) are used to put an imaginary space between words in variable names



# To determine the amount of cars not driven we subtract the amount of drivers (30) from the amount of cars (100), totaling 70 cars not dirven
cars_not_driven = cars - drivers

# The amount of cars driven is in congruance with the amount of drivers, which is 30
cars_driven = drivers

#The carpool capacity is determined by multiplying the cars driven (30) by the amount of space in each car (4), totaling 120 availble spaces/people
carpool_capacity = cars_driven * space_in_a_car

# To find the average of passengers per car, we divide the total amount of passengers(90) by the cars driven(30), which equals an average of 3 passengers per car
average_passengers_per_car = passengers / cars_driven


# When printing strings with variables, variables do not require open and closed quote symbols
# Commas are necessary when there are strings with variables. Use them to seperate the string from the variable
# If a variable is nested within the string, use a comma after the first part of the string, and after the variable itself
# Remember that the parts of the strings that are seperated by variable require open and closed quotes for each part

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
