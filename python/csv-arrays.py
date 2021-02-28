names = []  # Creating the empty arrays that the data will be read into
ages = []
f = open("people.csv", "r")  # Open the file in read mode

for line in f:  # Loop through every line in the csv file
    line = line.strip()  # Strip the lines of line breaks and spaces
    # Creates an array containing the values on each line
    data = line.split(",")
    # Adding the first part of the line (the name) to the names array
    names.append(data[0])
    # Adding the second part of the line (the age) to the ages array
    ages.append(data[1])

print(names)
print(ages)
