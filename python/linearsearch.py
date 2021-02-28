names = ["Finlay", "Oli", "Mark", "Harry"]  # List of names to search through


def linearsearch(target):  # Declare function which takes the target name as a parameter
    for name in names:  # Loops through every name in the names list
        if name == target:  # Checks if name is the target name
            print("Name is in the list")
            return  # Ends the function as the name has been found
    # Reaches this point if name hasn't been found as loop ends
    print("Name is not in the list")


linearsearch("Finlay")  # 'Name is in the list'
linearsearch("Obama")  # 'Name is not in the list'
