names = ["Finlay", "Oli", "Mark", "Harry", "Finlay"]  # List of names


def countoccurences(target):  # Declares function with target as parameter
    count = 0  # Sets the count to 0 initially
    for name in names:  # Loops through each name in the list
        if name == target:  # Checks if each name is the target name
            count += 1  # Adds 1 to the count for each match found
    return count  # Returns the final count


print(countoccurences("Finlay"))  # 2
print(countoccurences("Oli"))  # 1
print(countoccurences("Obama"))  # 0
