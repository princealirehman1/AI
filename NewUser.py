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
                students.write("\n\t\t\t{0}\t\t\t{1}\t\t\t{2}".format(profile["name"], profile["age"], profile["cnic"]))
data = NewUser("Name","Age","Cnic")
data.insertUserData( int(input("Enter Number Of Entries : ")))