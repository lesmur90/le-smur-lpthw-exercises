# +plus
# -minus
# /slash
# *asterick
# %percent
# <less-than
# >greater-than
# <= less-than-equal
# >= greater-than-equal

print("I will now count my chickens:")


# Remember to Divide first, then do addition -- otherwise your math will be wrong

print("Hens", 25 + 30 / 6)

# PEMDAS is applied here again: Multiply first
# The % is not used in a typical way. As opposed to what is commonly known as "percent," it is used a modulo
# The modulo uses the remainder of the division of the two numbers it seperates

print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

# This is a little tricky: First things first is to add the first three numbers before the minus sign (3+2+1=6)
# Next, determine the modulo number, and then divide the numbers seperated by the slash: 4 divided by 2 (modulo = 0) and 1 divdied by 4 (.25)
# Then you have: 6 - 5 + 0 - .25 + 6. 
# This leaves you with 1 - .25 + 6
# Lastly, you end up with .75 + 6 = 6.75
# Go figure...touch up on your elementary math!!!

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
