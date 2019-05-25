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