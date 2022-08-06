import csvkit
import pandas as pd
import pymongo
import os
import logging

#logging detail
logging.basicConfig(filename="mysql.log" , level=logging.DEBUG ,format='%(levelname)s  %(asctime)s %(message)s')

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)

class task1:
    def __init__(self):
        try:
            self.file_name = "E:/OneDrive - student.amity.edu/office/python & R/DataScience_ineuron/Ineuron_Assignment/class assignment/FitBit data.csv"

            os.system('csvsql --insert --db mysql+mysqlconnector://root:subho987@localhost:3306/ineuron_31july "'+file_name+'"')

            !csvsql -i mysql  "E:/OneDrive - student.amity.edu/office/python & R/DataScience_ineuron/Ineuron_Assignment/class assignment/FitBit data.csv"  >  "E:/OneDrive - student.amity.edu/office/python & R/DataScience_ineuron/Ineuron_Assignment/class assignment/FitBit_ddl.sql"


        except Exception as e:
            # logging.error(e)
            print(e)
        
    def task1_1(self):
        try:
            '''1. Read this dataset in pandas , mysql and mongodb '''
            
            fitbit_df = pd.read_csv(self.file_name)
            print(fitbit_df.head())
        except Exception as e:
            print(e)

obj1 = task1()
obj1.task1_1()