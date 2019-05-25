# *** Question 1 ***

print("Question: Store a message in a variable, and then print that message")

name = "ALI REHMAN"

print(name)

# *** Question 2 ***

print("Question: Store a message in a variable, and print that message."
      "Then change the value of your variable to a new message, and print the new message.\n")

message = "This is default message"

print(message)

message = input("Enter your new message: ")


print(message)

# *** Question 3 ***

print("Question: Store a person’s name in a variable, and print a message to that person."
      "Your message should be simple, such as, “Hello Shahzad,would you like to learn some Python today?”\n")

name = input("Please enter your name: ")

print("Hello {0},would you like to learn some Python today?".format(name))



# *** Question 4 ***

print("Question: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.\n")

name = input("Please enter your name: ")

print("Uppercase: {0}\n"
      "Lowercase: {1}\n"
      "Titlecase: {2}".format(name.upper(),name.lower(),name.title()))

# *** Question 5 ***

print("*** Question ***"
      "\n"
      "Find a quote from a famous person you admire."
      "\n"
      "Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:"
      "\n"
      "Albert Einstein once said, “A person who never made a mistake never tried anything new.”\n")

author = input("Please enter your author name: ")
quote = input("Please enter quote of your auther: ")

print("{0} once said, \"{1}\".".format(author,quote))

# *** Question 6 ***

print("\n"
      "*** Question ***"
      "\n"
      "Write addition, subtraction, multiplication, and division operations that each result in the number 8."
      "\n"
      "Be sure to enclose your operations in print statements to see the results."
      "\n"
      "You should create four lines that look like this: print(5 + 3)"
      "\n")

print("Addition: 7 + 1 = {0}".format(7+1))

print("Subtraction: 10 - 2 = {0}".format(10-2))

print("Multiplication: 4 * 2 = {0}".format(4*2))

print("Division : 64 / 8 = {0}".format(64/8))

# *** Question 7 ***

print("\n"
      "*** Question ***"
      "Create a variable called number1 with the value of 8."
      "\n"
      "Write a print statement to print number1 multiplied by 9."
      "\n")

number1 = 8

print("{0} * 9 = {1}".format(number1,number1*9))

# *** Question 8 ***

print("\n"
      "*** Question ***"
      "Store your favorite number in a variable. Then, using that variable, create a message that reveals your favorite number."
      "\n"
      " Print that message.")

fav_num = 5

print("Your fav number is {0}".format(fav_num))

# *** Question 9 ***

print("\n"
      "*** Question ***"
      "Store your name and your age in a varibale called my_name and my_age."
      "\n"
      "Use format method to print your name and your age."
      "\n"
      "Your final output sholud be like this:"
      "\n"
      "OUTPUT: "
      "\n"
      "My name is Shahzad Ahsan and my age is 21."
      "\n"
      "NOTE:Use both of the format methods which were discuss in the class.")

my_name = input("Please enter your name: ")
my_age = input("Please enter your age: ")

print("My name is {0} and my age is {1}".format(my_name,my_age))

# *** Question 10 ***

print("\n"
      "*** Question ***"
      "Write a Python program to check if a number is positive, negative or zero."
      "\n")

number = input("Please enter any number: ")

number = int(number)

if(number > 0):
    print("{0} is positive".format(number))
elif (number < 0):
    print("{0} is negative".format(number))
elif (number == 0):
    print("{0} is Zero".format(number))

# *** Question 11 ***

print("\n"
      "*** Question ***"
      "\n"
      "Write a Python program which accepts the radius of a circle from the user and compute the area."
      "\n")

radius = float(input("Please enter radius of a circle: "))
pie=float(3.144)

print("Area of a circle is : {0} ".format(pie*(radius*radius)))

# *** Question 12 ***

print("\n"
      "*** Question ***"
      "\n"
      "Write a Python function to check whether a number is completely divisible by another number."
      "\n"
      "Accept two integer values form the user")

num1 = int(input("Please enter num1 :"))
num2 = int(input("Please enter num2 :"))

result = num1%num2

result_message ="Null"

if(result==0):
    result_message="YES COMPLETELY DIVISBLE"
else:
    result_message = "NO, NOT COMPLETELY DIVISIBLE"

print("{0}/{1} = {2}".format(num1,num2,result))

print(result_message)

# *** Question 13 ***

print("\n"
      "*** Question ***"
      "Write a Python program to find whether a given number (accept from the user) is even or odd,"
      "\n"
      " print out an appropriate message to the user.")

num1 = int(input("Please enter num1 :"))

result = num1%2

result_message ="Null"

if result==0:
    result_message="{0} is EVEN".format(num1)
else:
    result_message = "{0} is ODD".format(num1)

print(result_message)

# *** Question 14 ***

print("\n"
      "*** Question ***"
      " Print a suitable statement that uses their response."
      "an"
      "Such as, if they entered “Bangkok”: “I’d love to visit Bangkook more often”"
      "\n")

use_response = input("Please enter anything: ")

print("I don't know what you mean by {0}".format(use_response))

# *** Question 15 ***

print("\n"
      "*** Question ***"
      "Write an input line to ask a user whether they want to take the red pill or the blue pill."
      "\n"
      "If they write “red” then print “You stay in wonderland and see how far the rabbit hole goes”."
      "\n"
      "Elif they write “blue” then print “You wake up in your bed and believe what you want to believe.”."
      "\n"
      "Else print “That’s not an option Neo.”")

pill = input("Would you like to have the RED PILL or the BLUE PILL: ").lower()

if pill.__contains__("red"):
    print("You stay in wonderland and see how far the rabbit hole goes")
elif pill.__contains__("blue"):
    print("You wake up in your bed and believe what you want to believe.")
else:
    print("That’s not an option Neo.")


