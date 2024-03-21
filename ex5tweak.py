# Use the the "format string" (or the f string) before open quotes for a string that uses variables using the special {} sequence

name = 'Zed A. Shaw'
age = 35 # not a lie
inches = 74 # inches
pounds = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# There are 2.54 cm for every inch. The conversion for inches to centimeters is the amount of inches multiplied by 2.54
# There are about 0.453592 kilograms for every pound. The amount of pounds multiplied by 0.453592 equals the kilogram conversion

centimeters = inches * 2.54
kilograms = pounds * 0.453592

print(f"Let's talk about {name}.")
print(f"He's height is {inches} inches tall.")
print(f"His height in centimeters is {centimeters}cm.")
print(f"He's {pounds} pounds heavy.")
print(f"His weight in kilograms would be {kilograms}kg.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + inches + pounds
print(f"If I add {age}, {inches}, and {pounds} I get {total}.")