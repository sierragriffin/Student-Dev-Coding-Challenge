# Sierra Griffin
# Task 3


def factorial_function(inputInteger):
    
    # Termination case
    if (inputInteger == 1):
        return 1

    # Recursive call to the function to calculate factorial
    # ex: 4 * 3 * 2 * 1
    else:
        return (inputInteger * factorial_function(inputInteger - 1))

print("\n") # For readability 
print(factorial_function(3))
print("\n") # For readability 