# Sierra Griffin
# Task 2

def largest_integer_function(inputList):
    
    # Create a variable to hold the largest integer 
    # Set this variable to be the first integer in the inputList
    largestInt = inputList[0]
    
    # Iterate through the integers in the inputList
    # If the value of the integer is greater than the value of the largestInt,
    # set that integer to be the new largestInt
    for i in range(0, len(inputList) - 1):
        if (inputList[i + 1] > largestInt):
            largestInt = inputList[i + 1]
    
    # Check the last integer in the inputList
    if inputList[len(inputList) - 1] > largestInt:
        largestInt = inputList[len(inputList) - 1] 
    
    return (largestInt)

print("\n") # For readability 
print(largest_integer_function([1, 3, 2]))
print("\n") # For readability 