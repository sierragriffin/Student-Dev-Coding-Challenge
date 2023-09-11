# Sierra Griffin
# Task 1

def reverse_function(inputString):

    # Reverse iterate through each letter in the inputString
    for letter in range(len(inputString) - 1, -1, -1):
        print(inputString[letter], end="")

print("\n") # For readability 
reverse_function("string")
print("\n") # For readability 