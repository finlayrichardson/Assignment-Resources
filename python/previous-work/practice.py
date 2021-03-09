def get_new():  # Gets information of new member
    first_name = input("Enter the first name: ")
    surname = input("Enter the surname: ")
    category = input("Enter the category: ")
    password = gen_pass()
    return first_name, surname, category, password


def gen_pass():  # Gets a valid password from the user
    valid = False
    while not valid:
        password = input("Enter the password: ")
        if ord(password[0]) >= 65 and ord(password[0]) <= 90:
            if ord(password[-1]) >= 35 and ord(password[-1]) <= 37:
                valid = True
    return password


def add_new(fname, sname, cat, pw):  # Puts data from csv file into arrays and adds new member
    firstName = [""] * 50
    surname = [""] * 50
    category = [""] * 50
    password = [""] * 50
    f = open('members.txt', 'r')
    index = 0
    for x in range(10):
        line = f.readline()
        line = line.strip()
        data = line.split(",")
        firstName[index] = data[0]
        surname[index] = data[1]
        category[index] = data[2]
        password[index] = data[3]
        index += 1
    firstName[10] = fname
    surname[10] = sname
    category[10] = cat
    password[10] = pw
    print("Our members are:")  # Prints the members and their categories
    for x in range(11):
        print(firstName[x], surname[x], category[x])
    return category


def count_cat(categories):  # Counts the number of members in each category
    adult = 0
    junior = 0
    senior = 0
    total = 0
    for category in categories:
        if category == "Adult":
            adult += 1
            total += 1
        elif category == "Junior":
            junior += 1
            total += 1
        elif category == "Senior":
            senior += 1
            total += 1
    print(f"There are currently {adult} Adult members")
    print(f"There are currently {junior} Junior members")
    print(f"There are currently {senior} Senior members")
    # Prints the total number of members
    print(f"Total current membership is {total}")


first_name, surname, category, password = get_new()
categories = add_new(first_name, surname, category, password)
count_cat(categories)
