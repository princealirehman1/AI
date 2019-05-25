# names = ["prince",1,2]
#
# names.insert(0,5)
# names.append(100)
# names.reverse()
#
# print(names[1])

# name = input("Please enter your name: ")
# age = input("Please enter your age: ")
#
#
# print("My name is {} and my age is {}".format(name,age))

names = ["AHMED","ALI","SAMI","FASIH","KAMRAN"]

subNames = names[2:names.__len__()]

# names.__delitem__(2)

# del names[2]

# print(len(subNames))
#
# print(names.pop(2))
# print(names)
#
# print(names.pop(2))
#
# print(names)
#
# print(f"Names: {names}\nSubNames: {subNames}")

# constantList = ("A",2)
#
# constantList1 = ("B",2)

# print("Tupple1 {}\nTupple2 {}".format(constantList,constantList1))

# print(constantList + constantList1)


# num1  = 10
# num2 = 3
#
# result = num1/num2
#
# print(int(result))
#
# numbers = [1,2,3,4,5,6,7,8,9,10]
#
# numbers.reverse()
#
# for number in numbers:
#     print(number)

# name = input("PLease enter your name: ")
#
# for c in name:
#     print(c)

#
# print(name.lower())
# print(name.upper())
# print(len(name))

# number = input("Please Enter Number: ")
# result = int(number) % 2
#
# if result == 0 :
#     print("EVEN")
# else:
#     print("ODD")

# HASH MAP

# hasmap = {"6802" : "PRINCE ALI","7802" : "HAIDER"}

# print(hasmap.get("6802"))

haveCNIC = input("Do you have CNIC: ")

if haveCNIC == "Yes":

    inVoterList = input("Are you in voter list: ")
    if inVoterList == "Yes":
        print("You can cast your Vote")
    else:
        print("You Cannot Cast Your Vote")
else:
    print("You cannpt cast your vote")