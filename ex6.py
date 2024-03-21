# A string is usually a bit of text you want to display to someone or "export" out of the program you are writing
# A variable is any line of code where you set a name=(equal) to a value

# This variable explains the that the types of people is equal to 10. It uses underscores to create space between each word.
types_of_people = 10

# This variable is represented by x (a common python character) and contains an format string.
# Using an f-string allows for the embedding of an expression directly into string literals.

x = f"There are {types_of_people} types of people."

# The following two lines, I believe, are for the sake of practice--otherwise, couldn't one simply write "binary" or "don't" d

binary = "binary"
do_not = "don't"

# Per the previous comment, if "binary" and "don't" were not variables, would the value assigned to name "y" need to use an f-string?

y = f"Those who know {binary} and those who {do_not}."

# Prints the name "x" which contains the vairable "types_of_people" in an f-string

print(x)

# Prints the name "y" which contains the variables "binary" and "do_not" in an f-string

print(y)

# Prints an f-string that contains the variable "x" whose value is an f-string...that contains a variable.

print(f"I said: {x}")

# "" "" "" "" that contains the variable "y" "" "" "" "" that contains variables.

print(f"I also said: '{y}'")

# A variable with the name "hilarious" having the value of "False".

hilarious = False

# This variable is interesting: It's value is a string literal that includes the special {} sequence with no data within it.
# Note: When the special {} sequence is empty, it is serving as a placeholder for future/customizable information.

joke_evaluation = "Isn't that joke so funny?! {}"

# .format methods are used to replace placeholders (usually in {}) with specific values.

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
