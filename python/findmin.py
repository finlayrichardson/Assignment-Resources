numbers = [1, 34, 4, 234, 8, 3434, 4]  # List of numbers


def findmin():  # You don't have to pass the array into the function because arrays are global
    # Set the initial minimum value to the first number in the list
    min = numbers[0]
    for num in numbers:  # Loops through the numbers in the list
        if num < min:  # Checks if each number is smaller than the current minimum
            min = num  # If so, sets the minimum to the new smallest number
    return min


print(findmin())  # 1
