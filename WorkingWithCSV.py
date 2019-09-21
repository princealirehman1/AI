import csv;

class WorkingWithCSV:

    def __init__(self):
        self.__dummyData = 'name,class,city,cell'

    def writeDataToCSV(self, csv_data , file_name):

        with open('./Data/{0}.csv'.format(file_name),'r') as u_csv:
            csv_write = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    def readDataFromCSV(self, ):