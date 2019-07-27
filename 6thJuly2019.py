class Car:

    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model

    def getYear(self):
        return self.__year

    def getCarDetails(self):
        return "Car Make: {0}\nCar Model: {1}\nCar Year: {2}".format(self.getMake(), self.getModel(), self.getYear())


myCar = Car("Honda", "Civic", 2016)


# print(myCar.getCarDetails())

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.__restaurant_name = restaurant_name
        self.__cuisine_type = cuisine_type
        self.__isOpen = "Yes"
        self.__numberServed = 0

    def describe_restaurant(self):
        return "*** {0} ***\nDeals in all {1}".format(self.__restaurant_name, self.__cuisine_type)

    def open_restaurant(self):

        if (self.__isOpen.__eq__("Yes")):
            return "Restaurant is Open"
        else:
            return "Restaurant is Close"

    def setRestorantIsOpen(self, isOpen):
        self.__isOpen = isOpen

    def setNumberServed(self, number):
        self.__numberServed = number

    def getCurrentServing(self):
        return "Currently Serving: {0}".format(self.__numberServed)

    def incrementNoServed(self):
        self.__numberServed += 1


# resto1 = Restaurant("ALI-BABA CUISINE","PAKISTANI FOODS")
# resto1.setRestorantIsOpen("Yes")
#
# resto2 = Restaurant("ANWAR BALOOCH","CHINEES FOODS")
# resto2.setRestorantIsOpen("No")
#
# resto3 = Restaurant("CHINTOSS","JAPANEES FOODS")
# resto2.setRestorantIsOpen("Yes")
# resto3.setNumberServed(5)
# resto3.incrementNoServed()
#
# print(resto1.describe_restaurant())
# print(resto1.open_restaurant())
# resto1.incrementNoServed()
# print(resto1.getCurrentServing())
#
# print("\n")
# print(resto2.describe_restaurant())
# print(resto2.open_restaurant())
# print(resto2.getCurrentServing())
#
# print("\n")
# print(resto3.describe_restaurant())
# print(resto3.open_restaurant())
# print(resto3.getCurrentServing())


class User():

    def __init__(self, first_name, last_name, age, city, hobbies):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__city = city
        self.__hobbies = hobbies

    def describe_user(self):
        return "*** USER PROFILE ***\nFirst Name: {0}\nLast Name: {1}\nAge: {2}\nCity: {3}\nHobbies: {4}".format(
            self.__first_name, self.__last_name, self.__age, self.__city, self.__hobbies)

    def greet_user(self):
        return ("*** Hello {0}, Have a njce day!".format(self.get_fistname()))

    def get_fistname(self):
        return self.__first_name;


u1 = User("ALI", "REHMAN", 21, "Karachi", "Watching Movies!")


# print(u1.describe_user())
# print(u1.greet_user())


class ElectricCar(Car):
    def __init__(self):
        super().__init__("Suzuki", "ALTO", 2019)
        self.__batterySize = "3200 mah"
        self.__battery = Battery("Osaka", 12, 20)
        self.__engine = Engine("Honda", "AXISO291SF", 20)

    def set_battery_size(self, batterySize):
        self.__batterySize = batterySize

    def get_batteryy_size(self):
        return self.__batterySize

    def getBatteryDetails(self):
        return "\n*** Battery Details ***\nMake: {0}\nVolts:{1}\nAmp:{2}".format(self.__battery.getMake(),
                                                                                 self.__battery.getVolts(),
                                                                                 self.__battery.getAmp())

    def getEngineDetails(self):
        return "\n*** Engine Details ***\nMake: {0}\nModel: {1}\nHorse Power {2}".format(self.__engine.getMake(),
                                                                                         self.__engine.getModel(),
                                                                                         self.__engine.getHp())


class Battery():

    def __init__(self, make, volts, amp):
        self.__make = make
        self.__volts = volts
        self.__amp = amp

    def getMake(self):
        return self.__make

    def getVolts(self):
        return self.__volts

    def getAmp(self):
        return self.__amp

    def setMake(self, make):
        self.__make = make

    def setVolts(self, volts):
        self.__volts = volts

    def setAmp(self, amp):
        self.__amp = amp


class Engine():
    def __init__(self, make, model, hp):
        self.__make = make
        self.__model = model
        self.__hp = hp

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model

    def getHp(self):
        return self.__hp


eCar = ElectricCar()


# print(eCar.getCarDetails())
# print(eCar.getBatteryDetails())
# print(eCar.getEngineDetails())

# with open("abc.txt","w") as file :
#     file.write("Yahoo, Chai koi mjhy jangli kahay ....... \n Kahnay do gi kehta rahay \n tan tan tana tan")
#
# with open("abc.txt","a") as file :
#     file.write("\nPOPOPOPPOPOPOPO\nKOKOKOKOKOKOKOKOKOKO")
#
# with open("abc.txt","r") as file :
#     print(file.read())

# import  requests
#
# request = requests.get("https://www.google.com/")
# print(request.text)
# print("\n\n*** THIS IS CONTENT ***\n\n")
# print(request.content)

# with open("abc.txt","r") as file :
#     print(file.read())

class NewUser:

    def __init__(self, name_label, age_label, cnic_label):
        self.__name_label = name_label
        self.__age_label = age_label
        self.__cnic_label = cnic_label

        with open("Students.txt", "w") as students:
            students.write("\t\t{0}\t\t{1}\t\t{2}".format(name_label,age_label,cnic_label))

    def insertUserData(self, noOfEntries):

        profiles = []

        for n in range(noOfEntries):
            name = input("{0} -- Student Name :".format(n))
            age = input(" {0} -- Student Age :".format(n))
            cnic = input("{0} -- Student Cnic :".format(n))

            print("\n\n")

            profiles.append(

                {
                    "name": name,
                    "age": age,
                    "cnic": cnic
                }
            )
        print("*** Writing Data To File ***")
        self.writeDataToFile(profiles)


    def writeDataToFile(self, profiles):

        for profile in profiles:
            with open("Students.txt", "a") as students:
                students.write("\n\t\t{0}\t\t{1}\t\t{2}".format(profile["name"], profile["age"], profile["cnic"]))
data = NewUser("Name","Age","Cnic")
data.insertUserData( int(input("Enter Number Of Entries : ")))
