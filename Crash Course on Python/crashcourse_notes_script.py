"""
Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".
"""


def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5))  # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 km


"""
The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends with the old string. If there is more than one occurrence of the old string in the sentence, only the one at the end is replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made). 
"""


def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = len(sentence) - len(old)
        new_sentence = sentence[:i] + new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"


"""
Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is on an even position or an odd position.
"""


def skip_elements(elements):
    # code goes here
    a = len(elements)
    return elements[0:a:2]


# Should be ['a', 'c', 'e', 'g']
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))


"""
The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using list comprehension. Hint: remember that list and range counters start at 0 and end at the limit minus 1.
"""


def odd_numbers(n):
    return [x for x in range(1, n + 1) if x % 2 != 0]


print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1))  # Should print []


"""
Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.
"""


filenames = ["program.c", "stdio.hpp",
             "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
newfilenames = []
# using as many lines of code as your chosen method requires.
for x in range(len(filenames)):
    if x <= len(filenames):
        if filenames[x].endswith("hpp"):
            result = filenames[x].replace('hpp', 'h')
            newfilenames.append(result)
        else:
            newfilenames.append(filenames[x])


print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


"""
Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.
"""


def pig_latin(text):
    say = ""
    # Separate the text into words
    q = []
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        q.append(word[1:] + word[0] + "ay")
        # Turn the list back into a phrase
    say = " ".join(q)
    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# Should be "rogrammingpay niay ythonpay siay unfay"
print(pig_latin("programming in python is fun"))


"""
The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted. For example: 640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----" 755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x" Fill in the blanks to make the code convert a permission in octal format into a string format. 
"""


def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for x in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if x >= value:
                result += letter
                x -= value
            else:
                result += "-"
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------


"""
The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.
"""


def group_list(group, users):
    members = ", ".join(users)
    return "{}: {}".format(group, members)


# Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))
# Should be "Engineering: Kim, Jay, Tom"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))
print(group_list("Users", ""))  # Should be "Users:"


"""
The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that.
"""


def guest_list(guests):
    for name, age, prof in guests:
        print("{} is {} years old and works as {}".format(name, age, prof))


guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'),
            ('Amanda', 25, "Engineer")])


"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""


"""
The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 1) Add an entry for Epilogue on page 39. 2) Change the page number for Chapter 3 to 24. 3) Display the new dictionary contents. 4) Display True if there is Chapter 5, False if there isn't.
"""

toc = {"Introduction": 1, "Chapter 1": 4,
       "Chapter 2": 11, "Chapter 3": 25, "Chapter 4": 30}
toc["Epilogue"] = 39  # Epilogue starts on page 39
toc["Chapter 3"] = 24  # Chapter 3 now starts on page 24
print(toc)  # What are the current contents of the dictionary?
print("Chapter 5" in toc)  # Is there a Chapter 5?


"""
Now, it's your turn! Have a go at iterating over a dictionary!

Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each element in the dictionary.
"""


cool_beasts = {"octopuses": "tentacles", "dolphins": "fins", "rhinos": "horns"}
for beasts, parts in cool_beasts.items():
    print("{} have {}".format(beasts, parts))


"""
In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a list containing multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their colors. Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.
"""


wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
for item in wardrobe:
    for key in wardrobe[item]:
        print("{} {}".format(key, item))


"""
The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).
"""


def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append("{}@{}".format(user, domain))
    return(emails)


print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": [
      "barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


"""
The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.
"""


def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():
        for user in users:
            user_groups.setdefault(user, []).append(group)
    return(user_groups)


print(groups_per_user({"local": ["admin", "userA"],
                       "public":  ["admin", "userB"],
                       "administrator": ["admin"]}))


"""
The add_prices function returns the total price of all of the groceries in the dictionary. Fill in the blanks to complete this function.
"""


def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for value in basket.values():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += value
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}


print(add_prices(groceries))  # Should print 28.44


"""
The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.
"""


def format_address(address_string):
    # Declare variables
    address = address_string.split(" ")
    # Determine if the address part is the
    # house number or part of the street name
    house_number = address[0]
    street_name = address[1:]
    # Does anything else need to be done
    # before returning the result?
    street_name = " ".join(street_name)

    # Return the formatted string
    return "house number {} on street named {}".format(house_number, street_name)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


"""
The highlight_word function changes the given word in a sentence to its upper-case version. For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line? 
"""


def highlight_word(sentence, word):
    return sentence.replace(word, word.upper())


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "laoud"))
print(highlight_word("Automating with Python is fun", "fun"))


"""
A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order. Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.
"""


def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    # Followed by the elements of list1 in reverse order
    return list2 + list1[::-1]


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))


"""
Use a list comprehension to create a list of squared numbers (n*n). The function receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively. For example, squares(2, 3) should return [4, 9].
"""


def squares(start, end):
    return [n * n for n in range(start, end + 1)]


print(squares(2, 3))  # Should be [4, 9]
print(squares(1, 5))  # Should be [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


"""
Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one.
"""


def car_listing(car_prices):
    result = ""
    for car, price in car_prices.items():
        result += "{} costs {} dollars".format(car, price) + "\n"
    return result


print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo": 55000,
                   "Ford Fiesta": 13000, "Toyota Prius": 24000}))


"""
Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, but Rory's list has more current information about the number of guests. Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. Then print the resulting dictionary.
"""


def combine_guests(guests1, guests2):
    # Combine both dictionaries into one, with each key listed
    # only once, and the value from guests1 taking precedence
    consolidated = {}
    consolidated.update(guests2)
    consolidated.update(guests1)
    return consolidated


Rorys_guests = {"Adam": 2, "Brenda": 3, "David": 1,
                "Jose": 3, "Charlotte": 2, "Terry": 1, "Robert": 4}
Taylors_guests = {"David": 4, "Nancy": 1,
                  "Robert": 2, "Adam": 1, "Samantha": 3, "Chris": 5}

print(combine_guests(Rorys_guests, Taylors_guests))


"""
Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}"""


def count_letters(text):
    result = {}
    text = ''.join(c for c in text.lower() if c.isalpha())
    # Go through each letter in the text
    for letter in text:
        # Check if the letter needs to be counted or not
        # Add or increment the value in the dictionary
        if letter not in result:
            result[letter] = 1
        else:
            result[letter] += 1
    return result


print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)


animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])


host_addresses = {"router": "192.168.1.1",
                  "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())


"""
Want to give this a go? Fill in the blanks in the code to make it print a poem.
"""


class Flower:
    color = 'unknown'


rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "blue"

this_pun_is_for_you = "Dude!"

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you)


"""
Creating new instances of class objects can be a great way to keep track of values using attributes associated with the object. The values of these attributes can be easily changed at the object level. The following code illustrates a famous quote by George Bernard Shaw, using objects to represent people. Fill in the blanks to make the code satisfy the behavior described in the quote. 
"""

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw


class Person:
    apples = 0
    ideas = 0


johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1


def exchange_apples(you, me):
    # Here, despite G.B. Shaw's quote, our characters have started with
    # different amounts of apples so we can better observe the results.
    # We're going to have Martin and Johanna exchange ALL their apples with #one another.
    # Hint: how would you switch values of variables,
    # so that "you" and "me" will exchange ALL their apples with one another?
    # Do you need a temporary variable to store one of the values?
    # You may need more than one line of code to do that, which is OK.
    temp = you.apples
    you.apples = me.apples
    me.apples = temp
    return you.apples, me.apples


def exchange_ideas(you, me):
    # "you" and "me" will share our ideas with one another.
    # What operations need to be performed, so that each object receives
    # the shared number of ideas?
    # Hint: how would you assign the total number of ideas to
    # each idea attribute? Do you need a temporary variable to store
    # the sum of ideas, or can you find another way?
    # Use as many lines of code as you need here.
    temp = you.ideas
    you.ideas += me.ideas
    me.ideas += temp
    return you.ideas, me.ideas


exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(
    johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(
    johanna.ideas, martin.ideas))


"""
The City class has the following attributes: name, country (where the city is located), elevation (measured in meters), and population (approximate, according to recent statistics). Fill in the blanks of the max_elevation_city function to return the name of the city and its country (separated by a comma), when comparing the 3 defined instances for a specified minimal population. For example, calling the function for a minimum population of 1 million: max_elevation_city(1000000) should return "Sofia, Bulgaria". 
"""

# define a basic city class


class City:
    name = ""
    country = ""
    elevation = 0
    population = 0


# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509


def max_elevation_city(min_population):

    # Initialize the variable that will hold
    # the information of the city with
    # the highest elevation
    return_city = City()

    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city1.population >= min_population and city1.elevation > return_city.elevation:

        return_city = city1
    # Evaluate the 2nd instance to meet the requirements:
    # does city #2 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city2.population >= min_population and city2.elevation > return_city.elevation:
        return_city = city2
    # Evaluate the 3rd instance to meet the requirements:
    # does city #3 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city3.population >= min_population and city3.elevation > return_city.elevation:
        return_city = city3

    # Format the return string
    if return_city.name:
        return ("{}, {}".format(return_city.name, return_city.country))
    else:
        return ""


print(max_elevation_city(100000))  # Should print "Cusco, Peru"
print(max_elevation_city(1000000))  # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000))  # Should print ""


"""
We have two pieces of furniture: a brown wood table and a red leather couch. Fill in the blanks following the creation of each Furniture class instance, so that the describe_furniture function can format a sentence that describes these pieces as follows: "This piece of furniture is made of {color} {material}"
"""


class Furniture:
    color = ""
    material = ""


table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"


def describe_furniture(piece):
    return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))


print(describe_furniture(table))
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch))
# Should be "This piece of furniture is made of red leather"


"""
Let’s test your knowledge of using dot notation to access methods and attributes in an object. Let’s say we have a class called Birds. Birds has two attributes: color and number. Birds also has a method called count() that counts the number of birds (adds a value to number). Which of the following lines of code will correctly print the number of birds? Keep in mind, the number of birds is 0 until they are counted!
"""


class Birds:
    color = ""
    number = 0


bluejay = Birds()
bluejay.color = "blue"
bluejay.number = 1

print(bluejay.number)


"""
OK, now it’s your turn! Have a go at writing methods for a class. Create a Dog class with dog_years based on the Piglet class shown before (one human year is about 7 dog years).
"""


class Dog:
    years = 0

    def dog_years(self):
        return self.years * 7


fido = Dog()
fido.years = 3
print(fido.dog_years())


"""
Want to see this in action? In this code, there's a Person class that has an attribute name, which gets set when constructing the object. Fill in the blanks so that 1) when an instance of the class is created, the attribute gets set correctly, and 2) when the greeting() method is called, the greeting states the assigned name.
"""


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)


# Create a new instance with a name of your choice
some_person = Person("steph")
# Call the greeting method
print(some_person.greeting())


"""
Remember our Person class from the last video? Let’s add a docstring to the greeting method. How about, “Outputs a message with the name of the person”.
"""


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        "Outputs a message with the name of the person"
        print("Hello! My name is {name}.".format(name=self.name))


help(Person)


"""
The code below defines an Elevator class. The elevator has a current floor, it also has a top and a bottom floor that are the minimum and maximum floors it can go to. Fill in the blanks to make the elevator go through the floors requested.
"""


class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = 0
        self.top = 10
        self.current = 0

    def up(self):
        """Makes the elevator go up one floor."""
        if self.current == 10:
            self.current += 0
        else:
            self.current += 1

    def down(self):
        """I'm assuming the lowest floor the elevator can go is -1"""
        """Makes the elevator go down one floor."""
        if self.current <= -1:
            self.current -= 0
        else:
            self.current -= 1

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor

    def __str__(self):
        return "Current floor: {}".format(self.current)


elevator = Elevator(-1, 10, 0)
elevator.up()
print(elevator.current)  # should output 1
elevator.down()
print(elevator.current)  # should output 0
elevator.go_to(10)
print(elevator.current)  # should output 10
# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current)  # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current)  # should be 1
elevator.go_to(5)
print(elevator)


"""
Let’s create a new class together and inherit from it. Below we have a base class called Clothing. Together, let’s create a second class, called Shirt, that inherits methods from the Clothing class. Fill in the blanks to make it work properly.
"""


class Clothing:
    material = ""

    def __init__(self, name):
        self.name = name

    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))


class Shirt(Clothing):
    material = "Cotton"


polo = Shirt("Polo")
polo.checkmaterial()


"""
Let’s expand a bit on our Clothing classes from the previous in-video question. Your mission: Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock. When you’re finished, the script should add up to 10 cotton Polo shirts. 
"""


class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class shirt(Clothing):
    material = "Cotton"


class pants(Clothing):
    material = "Cotton"


polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)


"""
Animals at the Zoo Jupyter notebook
"""


class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category


class Turtle:
    name = ""
    category = "reptile"

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category


print(Turtle.category)


class Snake:
    name = ""
    category = "reptile"

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category


print(Snake.category)


class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result


zoo = Zoo()


turtle = Turtle("Turtle")  # create an instance of the Turtle class
snake = Snake("Snake")  # create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

# how many zoo animal types in the reptile category
print(zoo.total_of_category("reptile"))