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