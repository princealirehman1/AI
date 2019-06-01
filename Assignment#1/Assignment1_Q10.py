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