numbers = [1, 34, 4, 234, 8, 3434, 4]  # List of numbers


def findmax():  # You don't have to pass the array into the function because arrays are global
    # Set the initial maximum value to the first number in the list
    max = numbers[0]
    for num in numbers:  # Loops through the numbers in the list
        if num > max:  # Checks if each number is larger than the current maximum
            max = num  # If so, sets the maximum to the new largest number
    return max


print(findmax())  # 3434
