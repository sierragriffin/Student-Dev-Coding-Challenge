# Sierra Griffin
# Task 4

def fibonacci_function(entryNumber):

    x = 1
    # Create and set position variables for the two values in the sequence that will be summed
    positionA = 1
    positionB = 0

    # Loop through this code until entryNumber is reached 
    # Calculate the new value for the fibonacci sequence (positionC) by 
    # summing the two previous numbers of the sequence (postionA and positionB)
    while x <= entryNumber:
        positionC = positionA + positionB
        # Set the new positions for calculating the next number in the sequence 
        positionA = positionB
        positionB = positionC
        # Iterate
        x = x + 1
    
    return positionC

print("\n") # For readability 
print(fibonacci_function(7))
print("\n") # For readability 