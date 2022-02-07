# Import panadas which can read url link
import pandas as pd
# Import other class
from readcsv import Data_Read_Csv as db
from model import Model
import timeprint
import time



def instuction():
    '''
     CST8333 Section 350
     Student Name: Jing Zhao
     Student ID: 040994750
     Assignment #2
     version 1.2
    '''
class Controller:
    list = []
    header = []
    temp_table = []

    # def __init__(self):
    #     pass
    #
    # def main(self):
    #     self.view.showMenu()


    def read_all(self):
    # try to link csv file in url format, if the path has issue, then throw exception
        try:
            #set csv path to a variable data_path
            csv_file = 'https://www.cer-rec.gc.ca/open/incident/pipeline-incidents-comprehensive-data.csv'
            #call Data_Read_Csv class in readcsv.py and display tail 10 lines, use variable data_pipeline as refernce in future use
            data_pipeline = db(csv_file).read().head(101)
# loop over the csv data table, create a list table_row for store each row from the csv file
# Pandas' dataframe to read data like excel, which use column name as index, row as line id
# eg table[1][1]-->[1] reflect excel Column A, row is line 1

            for i in range(len(data_pipeline[0])):
                row_content = (Model(data_pipeline[0][i], data_pipeline[1][i], data_pipeline[2][i], data_pipeline[3][i],
                                     data_pipeline[4][i], data_pipeline[5][i], data_pipeline[10][i], data_pipeline[12][i],
                                     data_pipeline[17][i]))
                # if i==0:
                #     self.header.append(row_content)
                # else:
                self.list.append(row_content)
            self.header.append(self.list[0])
        except:
            print("CSV file read error")


    def show_rows(self, displayRows):
        try:
            for num in displayRows:
                self.temp_table.append(self.list[num])
                return self.temp_table
        except:
            print("Error happen, please make sure input integer")


    def write_file(self):
        dataFrame=[]
        for obj in self.list:
            dataFrame.append(obj.toList())
        newFile = pd.DataFrame(dataFrame)
        newFile.to_csv('newFile.csv')

    def add_record(self, input_string):
        try:
            newContent = input_string.split(",")
            newRecord = Model(newContent[0], newContent[1], newContent[2], newContent[3], \
                          newContent[4], newContent[5], newContent[6], newContent[7], newContent[8])
        except:
            print("must have 9 contents")
        self.list.append(newRecord)


    def update_record(self, rowNum, input_string):
        try:
            newContent = input_string.split(",")
            newRecord = Model(newContent[0], newContent[1], newContent[2], newContent[3], \
                              newContent[4], newContent[5], newContent[6], newContent[7], newContent[8])
            self.list.remove(self.list[rowNum])
            self.list.insert(rowNum, newRecord)
        except:
            print("must have 9 contents")
        return self.list


    def delete_record(self, rowNum):
        try:
            self.list.remove(self.list[rowNum])
        except:
            print("Something wrong. Table has ", len(self.list), "rows only")
        return self.list


    def display(self):
        for row in self.list:
            print(row.toString())


    def displayTempTable(self):
        for row in self.temp_table:
            print(row.toString())


    def option(self):
        self.view.optionNum()


    def show_header(self):
        for name in self.header:
           return name.toList()


