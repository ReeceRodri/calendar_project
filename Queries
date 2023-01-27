import os 
import csv
from datetime import date

class Queries:
    
    def __init__(self):
        self.file_name = "event_data_base.csv"
        # Creating a database file if it doesn't exist 
        is_Exist = os.path.exists(self.file_name)
        if is_Exist:
            pass
        else:
            with open(self.file_name, "w") as  creating_csv_file:
                pass

#method to read the file
    def read_file(self):
        with open(self.file_name, 'r') as f:
            reader = csv.reader(f)
            self.data = list(reader)
            print(f'File {self.file_name} has been read.')
#method to display all rows
    def display_rows(self):
        for row in self.data:
            print(row)
#Just in case : method to display all columns
    def display_columns(self):
        for i in range(len(self.data[0])):
            column = []
            for row in self.data:
                column.append(row[i])
            print(column)
#writing to a file
# has to be called in the save command button   (update: insted of rewriting old data we want to get new row and add it to the csv file)       
    def write_file(self, new_record):
        with open(self.file_name, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(new_record)

            print(f'File {self.file_name} has been written.')

# checking current date and returning the entire row (update: 1. give and option to give the date and return values according to it
#                                                             2. instead of returning one row -> returns all the rows which are coresponding to a given date)          
    def check_date(self, date):
        return_list = []
        for row in self.data:
            if row[1] == date:
                return_list.append(row)
        return return_list


