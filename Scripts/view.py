#display menu options for the users to view
import time

from controller import Controller


class View:
    def __init__(self):
        self.controller = Controller()

    def showMenu(self):
        '''
        This is the menu after running project give user option to choice
        :return: no return
        '''
        print()
        print("--------------------- MENU ---------------------")
        print("1. reload the data from the csv file")
        print("2. display first 100 records from csv file")
        print("3. write a new file")
        print("4. display one record or multiple records")
        print("5. add a new record")
        print("6. edit an existing record")
        print("7. delete an existing record")
        print("0. exit")

    def optionNum(self):
        try:

            try:
                print("enter your choice: ")
                option = int(input(""))
            except:
                print("must enter an integer")

            if option == 1:
                print("reload the data from the csv file")
                self.controller.read_all()

            elif option == 2:
                print("display first 100 records from csv file")
                self.controller.display()

            elif option == 3:
                print("write a new file")
                self.controller.write_file()

            elif option == 4:
                print("display one record or multiple records")
                print("How many rows you want to display?")
                numDisplay = int(input(""))
                if numDisplay == 0:
                    print(self.controller.show_header())
                else:
                    displayRows=[]
                    print("enter rows you want to display")
                    i = 0
                    while i < numDisplay:
                        displayRows.append(int(input()))
                        i += 1
                    self.controller.show_rows(displayRows)
                    self.controller.displayTempTable()

            elif option == 5:
                print("add a new record")
                str = "input the data you want to insert seperate by comma"
                print(str)
                input_string = input(" ")
                self.controller.add_record(input_string)
                self.controller.display()

            elif option == 6:
                print("edit an existing record")
                print("enter the row you want to change")
                rowNum = int(input(""))
                print(self.controller.list[rowNum].toString())

                print("input the data you want to insert seperate by comma")
                input_string = input("")
                self.controller.update_record(rowNum, input_string)
                self.controller.display()

            elif option == 7:
                print("delete an existing record")
                print("length of table before delete:", len(self.controller.list))
                self.controller.display()
                print("enter the row you want to delete")
                rowNum = int(input(""))
                print(self.controller.list[rowNum].toString())
                time.sleep(4)
                self.controller.delete_record(rowNum)
                self.controller.display()

            elif option == 0:
                print("Thank you Bye")
                exit();

            elif option == 8:
                print("what you want to find: ")
                str= input('')
                print(self.controller.list.find(str))

            else:
                print("wrong input please enter again")
                self.showMenu()
                self.showMenu()
        except:
            print("Something wrong in option")


