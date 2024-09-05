# Write a Python program to reverse a string.
# Function to reverse a string
def reverse_string(input_string):
    # Reversing the string using slicing
    return input_string[::-1]

# Input string
string = "Hello, World!"
# Calling the function
reversed_string = reverse_string(string)

# Output the reversed string
print("Original String:", string)
print("Reversed String:", reversed_string)
