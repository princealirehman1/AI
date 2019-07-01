
# names=["ALI","REHMAN","FASIH","KHAN","ALTAF"]
#
# def myFunction():
#     for n in names:
#         print(n)
#
#     print("LOOP ENDED")
#
# myFunction()

# def printMyName(name,count):
#
#     num = int(count)
#     for n in range(num):
#         print(name)
#
#
# printMyName("PRINCE ALI",10000)

# def unlimitedParams(*specs):
#     print(specs)
#
# unlimitedParams("PRINCE","SAMI","YAHOOO",12390,12)


# def multiplyNumbs(num1,num2):
#
#     num1 = int(num1)
#     num2 = int(num2)
#
#     return num1*num2
#
# print(multiplyNumbs(2,2))


# names = ["ALI","ALITAF","FAROOQ"]
#
# def makeThemKhan(names):
#     for n in names:
#         print("{0} {1}".format(n,"KHAN"))
#
# makeThemKhan(names)

# *** Notes ***
# Single * is for normal value only arguments
# Double ** is for keypair arguments


# *** PIZZA ORDER ***

# def makeYourPizzaOrder(name,address,size,flavor,noOfToppings,*toppings):
#
#     print("\n*** Your Ordered Pizza ***\nSize: {0}\nFlavor: {1}\nToppings: {2}".format(size,flavor,parseTopping(toppings)))
#
# def parseTopping(topping):
#
#     availableToppings = ["Cheese","Red Chilli","Jalapino","Olives"]
#
#     top=""
#     for toping in topping:
#
#         top = top + "{0} ".format(toping)
#
#     return top
#
#
# def getname():
#
#     name = input()
#
#     return name
#
# def getaddress():
#     address = input()
#     return address
#
# def getsize():
#     pizzaSize = input()
#     return pizzaSize
#
# def getflavor():
#     flavor = input()
#     return flavor
#
# def getNoOfToppings():
#     noOfToppings = input()
#
#     return noOfToppings
#
# def getToppings():
#
#     availableToppings = ["Cheese","Red Chilli","Jalapino","Olives"]
#
#     count=0
#     userEnteredToppings=[]
#     while(getNoOfToppings()>count):
#
#         for at in availableToppings:
#             if availableToppings.__contains__(at):
#                 userEnteredToppings.append(at)
#             else:
#                 print("*** Sorry {}")
#
#
# name = print("*** Pizza Ultimate Order Form ***\nStep 1: Please Enter Your Name: {1}\nStep 2: Please Enter Your Address: {2}\nStep 3: Please enter your required size: {3}\nStep 4: Please enter your required flavor: {4}\nStep 5: How many toppings you want to enter: {5}\nStep 6: Please enter your toppings: {6}".format(getname(),getaddress(),getsize(),getflavor,getNoOfToppings(),getToppings()))
#
# makeYourPizzaOrder("Large","Spicy Italian","Extra Cheese","Spicy Jalapino")


# def keyPairArgs(**args):
#     print(print(args))
#
#
# keyPairArgs(age=25,address="akdjlaskjld")

# name = "ASIF"
#
# def getname(self,newName):
#     self.name = "KAMRAN"
#
# getname(self,"Farooq")

# class testing():
#
#     name = "PRINCE ALI"
#
#     def __init__(self):
#
#
#     def getname(self):
#         self.name = "IMRAN KHAN"
#
#
# print(testing().getname())

class Patient():

    def __init__(self,name=None,age=None,gender=None,bemari=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.bemari = bemari

    def __init__(self,name=None,age=None,gender=None,bemari=None,location=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.bemari = bemari
        self.location = location

p1 = Patient("ALI",25,"Male","Fever")

p2 = Patient("ALI",25,"Male","Fever","Lahore")


print(p1.name)
print(p1.age)
print(p1.gender)
print(p1.gender)

print(p2.name)
print(p2.age)
print(p2.gender)
print(p2.)
