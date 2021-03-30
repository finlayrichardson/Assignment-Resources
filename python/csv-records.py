from dataclasses import dataclass  # Imports the dataclass


@dataclass  # Decorator specifiying that we are making a record
class Person:  # Naming the record
    # Each property of the record and its type (can be str, int, float or bool)
    name: str
    age: int


# Creating the empty array of records with space for 5 records
people = [Person("", 0) for _ in range(5)]
f = open("people.csv", "r")  # Opening the file in read mode
index = 0  # Starts the index at 0 because arrays start at 0

for line in f:  # Loop through every line in the csv file
    line = line.strip()  # Strip the lines of line breaks and spaces
    # Creates an array containing the values on each line
    data = line.split(",")
    # Takes the record in the array at the corresponding index, and sets the name to the name on this line of the csv file
    people[index].name = data[0]
    # Does the same for age, as it is the second part of the line
    people[index].age = data[1]
    index += 1  # Increments the index after each loop

print(people)  # Prints the populated array of records with data from the csv file
