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

print("Hens", 25.0 + 30.0 / 6.0)

# PEMDAS is applied here again: Multiply and Divide first, then Add and Subtract. All from left to right
# The % is not used in a typical way. As opposed to what is commonly known as "percent," it is used a modulo
# The modulo uses the remainder of the division of the two numbers it seperates

print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)

print("Now I will count the eggs:")

# This is a little tricky: First things first is to do the necessary division (4 /2=0[your modulo] and 1/4=.25)
# Thus, you end up with 3 + 2 + 1 - 5 + 0 -.25 + 6
# Next, +plus the numbers starting from the left before you get to the -minus: 6 - 5 + 0 - .25 + 6. 
# This leaves you with 1 - .25 + 6
# Lastly, you end up with .75 + 6 = 6.75
# Go figure...touch up on your elementary math!!!

print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

print("Is it true that 3.0 + 2.0 < 5.0 - 7.0?")

print(3.0 + 2.0 < 5.0 - 7.0)

print("What is 3.0 + 2.0?", 3.0 + 2.0)
print("What is 5.0 - 7.0?", 5.0 - 7.0)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5.0 > -2.0)
print("Is it greater or equal?", 5.0 >= -2.0)
print("Is it less or equal?", 5.0 <= -2.0)
