import random

# Define a list of characters to use in the pattern
chars = ["*", "-", "+", "x", "o"]

# Define the size of the pattern
width = 10
height = 5

# Generate the pattern
pattern = ""
for y in range(height):
    for x in range(width):
        pattern += random.choice(chars)
    pattern += "\n"

# Print the pattern
print("Random pattern:")
print(pattern)