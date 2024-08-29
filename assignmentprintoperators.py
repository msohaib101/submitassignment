# ***************************************Print statement

# Printing a simple string
print("Hello, World!")

# Printing variables
name = "Sohaib"
age = 21
print("Name:", name)
print("Age:", age)

# printing the mixture of strings and integers
print("The Sum of", 5, "and", 10, "is:", 5 + 10)

# Using seperater and End
print("Sohaib", "Ali", "Hamza", sep=",")

print("Hello!", end="****")

# Printing List and Dictionary
fruits = ["banana", "Apple", "Mango"] 
print(fruits)
dictionary = ["Name:", "Muhammad Sohaib", "Age:", 21]

# printing with f string

name = "Sohaib"
height = 6
print(f"I am {name}, and my height is {height}ft")

# *******************************Strings

string1 = "Hello World"
string2 = 'Hello World'
string3 = """In it we can write anything and the same pattern will be printed
as we have written like "my name is Sohaib" """

# we can also access any word in a string
access_string = "Python"
first_word = access_string[0]
last_word = access_string[-1]
# in slicing the counting start from our first digit but end at one before like this ends on 3 instead of 4
middle_words = access_string[1:4]    
print(first_word)
print(last_word)
print(middle_words)

# adding two strings
addition = "Hello"+" "+"World"
print(addition)

# repeating a string
repeat = "ha" * 3
print(repeat)

# operations on strings
# length operation
opera = "    i Love pYthOn     "
lenght1 = len(opera)
print(lenght1)

# upper case operation
upper_case = opera.upper()
print(upper_case)

# lower case operation
lower_case = opera.lower()
print(lower_case)

# proper lower and upper case operation
striping_case = opera.strip()
print(striping_case)

# replacing a string
replacing_case = opera.replace("Love", "Hate")
print(replacing_case)

# spliting operation 
spliting_case = opera.split()
print(spliting_case)

# string formating

name = "Muhammad Sohaib"
age = 21
# st.format formating
formated_case = "name: {}, age: {}".format(name, age)
print(formated_case)
# f function formating
print(f"name:{name}, age: {age} ")

# Escape sequences
# \t Tab space
# \n new Line
# \\ Backslash
# \' single qoute
# \" Double qoute


# \t Tab space
sequences_check = "\t Escape Sequence Checks \t"
print(sequences_check)
# \n new Line
sequences_check = "\n Escape \n Sequence Checks \n"
print(sequences_check)
# \\ Backslash
sequences_check = "\\ Escape \\ Sequence Checks \\"
print(sequences_check)
# \' single qoute
sequences_check = "\' Escape \' Sequence Checks"
print(sequences_check)
# \" Double qoute
sequences_check = ' \" Escape \" Sequence Checks'

# ******************************f-Strings
# simple use of f string
my_name = "sohaib"
print(f"my name is {my_name}")

# using integers in f-strings

x = 10
y = 5

print(f"{x} + {y} = {x+y}")

# function calls
def square(n):
    return n*n

num = 4 
results = f"the square of {num}, is {square(num)}"
print(results)

#  ********************************Operators
# Addition
x = 5 + 10 
print(x)
# subtraction
x = 5-10
print(x)
# Multiplication
x = 5 * 10
print(x)
# Division
float = 5 / 10
print(x)
# floor division
x = 5//10
print(x)
# reminder
x = 5%10
print(x)
# exponentiation (raise to power)
x = 5**10
print(x)

# comparison operators
# equals to
x = ( 5==3 )
print(x)
# not equals to 
x = ( 5!=3 )
print(x)
# greater then
x = ( 5>3 )
print(x)
# smaller then
x = ( 5<3 )
print(x)
# greater then or equals
x = ( 5>=3 )
print(x)
# smaller then or equals 
x = ( 5<=3 )
print(x)

# operators of logic
# and operator in it if both are true then it will be true otherwise not
x = (5>3 and 5<3)
print(x)
# or operator in it if one of all values is true then the result is true
x = (5<3 and 5>3)
print(x)
# not operator it change the result and gives the output in reverse
x = not(3<5)
print(x)

# membership operators
# in operator 
x = "a" in "apple"
print(x)
# not in operator 
x = "b" not in "apple"
print(x)

# ************************Lists

simple_list = ["apple", "banana", "Mango"]
print(simple_list[1])
# mixed list
mixed_list = [1, "Sohaib", 1.653, [1, 2, 3, 4]]
mixed_list.append("work")
mixed_list.extend("emote")
print(mixed_list)
# simple operations on lists

main_list = ["apple", "banana", "Mango", "fruit", "Strawberry"]
# append add anything at the end of the given list
main_list.append("Grape")
print(main_list)
# extend it can add multiple items in the given list
main_list.extend(["Sohaib", "Work place", "Pyhton"])
print(main_list)
# insert it add a new item in the given list but add at a specific place
main_list.insert(2, "Anar")
print(main_list)
main_list.remove("banana")
print(main_list)
last = main_list.pop()
print(last)
main_list.clear()
print(main_list)

# ***************************Tuple
# creating simple tuples
tuple1 = (1, 2, 3, 4)
print(tuple1)
# another simple tuple
tuple1 = 1, 2, 3, 4
print(tuple1)
# another tuple in in tuple and all mixed
my_tuple = (1, 2, (3, 4, 5), [6, 7, 8], "Sohaib", 3.892, "dictionary")
print(my_tuple)
# mixed tuple
my_tuple1 = (1, 2, 3, "Sohaib", 3.5201)
print(my_tuple)
# accessing tuple 
acc_tuple = (1, 2, 3, "Work", 4)
print(acc_tuple[3])
# single element tuple
single_element_tuple = (1,)
print(single_element_tuple)
# single element tuple error getting
single_element_tuple2 = (1)
print(single_element_tuple2)
# adding two tuples
first_tuple = "Muhammad"
second_tuple = "Sohaib"
complete_tuple = first_tuple + second_tuple
print(complete_tuple)
# repeating tuples by any many times
start_tuple = (1, 2, 3)
repeat_tuple = start_tuple * 2
print(repeat_tuple)
# getting the lenght of a tuple
main_tuple = (1, 2, 3, 4, 5, 6)
lenght_tuple = len(main_tuple)
print(lenght_tuple)
# checking the existance of any element in a tuple
existance_tuple = (1, 2, 3, 4, 5)
exists = 3 in existance_tuple
print(exists)
# tuples by using for loops
mixed = (1, 2, (3, 4, 5), [6, 7, 8], "Sohaib", 3.892, "dictionary")
for fruit in mixed:
    print(fruit)
main_tuple1 = (1, 2, 3, 4, 5, 6)
lenght_tuple3 = len(main_tuple1)
print(lenght_tuple)

# *****************************For Loop
# creating simple for loops 
fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print(fruit)
# for loop for a mixed list
mixed = (1, 2, (3, 4, 5), [6, 7, 8], "Sohaib", 3.892, "dictionary")
for fruit in mixed:
    print(fruit)
# for loop for letters in a word
word = "Sohaib"
for letter in word:
    print(letter)
mixed_word = 1, 2, "Sohaib", 3.7829
for letters in mixed_word:
    print(letters)
# use of range in for loop
for i in range(5):
    print(i)
for i in range(9):
    print(i)
# assigning the things and writing them in a correct pattern by using for loop
grades = {"Sohaib": 85, "Ali": 92, "Hamza": 78}
for grade in grades:
    print(grade)

grades = {"Sohaib": 85, "Ali": 92, "Hamza": 78}
for student, grade in grades.items():
    print(f"{student}, got a grade of {grade}")
# for loop with if and else function
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        print("Found 3!")
        break
else:
    print("Sorry 3 was not found")
# for loop for squares
square_value = [x**2 for x in range(10)]
print(square_value)

# *********************************Input Handling
# simple input to handle
name = input("Enter your name:")
print(f"Hello, {name}")
# conversion of a string into integer in taking input 
age1 = input("Enter your age: ")
age = int(age1)
print(f"You are {age} years old")
# making input with different way
question = input("Enter your name and age with a space: ")
name, age = question.split()
age = int(age)
print(f"Name: {name}, Age: {age}")
# using try in input handling
try:
    ask = int(input("Enter your age:"))
    print(f"You are {ask} years old")
except ValueError:
    print("Enter a valid number")
# giving a default name for easy of user
get_name = input("Enter your name (By default is Guest)") or "Guest"
print(f"Hello, {get_name}")
# handling value error and taking a proper input
while True:  # Start of the loop
    age3 = input("Enter your age (or type and enter 'quit' to exit): ")
    if age3.lower() == 'quit':  # This is inside the loop
        print("Goodbye!")
        break  # This is inside the loop and will exit the loop when 'quit' is entered
    try:
        age = int(age3)
        print(f"You are {age} years old.")
    except ValueError:
        print("That's not a valid number. Please try again.")
