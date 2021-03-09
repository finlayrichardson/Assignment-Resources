from dataclasses import dataclass


@dataclass  # Creating the record structure for the beaches.
class Beach:
    name: str
    rating: int


# Reads the beach data from the csv file into the record structure.
def read_data():
    beaches = [Beach("", 0) for x in range(973)]
    f = open("beachData.csv", "r")
    index = 0
    for line in f:
        line = line.strip()
        data = line.split(",")
        beaches[index].name = data[0]
        beaches[index].rating = int(data[1])
        index += 1
    return beaches


# Calculates the average rating of the beaches without a rating of 5.
def calc_average(beaches):
    total = 0
    counter = 0
    for beach in beaches:
        if beach.rating != 5:
            total += beach.rating
            counter += 1
    average = total / counter
    return average


# Displays the average rating of all the beaches.
def display_average(average):
    print(f"The average rating for all beaches is {average}")


# Finds the beaches with the desired rating provided by the user.
def find_rating(beaches):
    target = int(input("Enter the rating of the beaches you want to see: "))
    for beach in beaches:
        if beach.rating == target:
            position = 0
            for x in range(len(beach.name)):
                if beach.name[x] == " " and position == 0:
                    position = x
            if position == 0:
                print(beach.name)
            else:
                print(beach.name[0:position])


beaches = read_data()
average = calc_average(beaches)
display_average(average)
find_rating(beaches)
