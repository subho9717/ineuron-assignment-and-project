import logging
from mysql.connector import connect
logging.basicConfig(filename="oops_function.log" , level=logging.DEBUG ,format='%(levelname)s  %(asctime)s %(message)s')


"""ineuron login"""
class oops_function:
    def __init__(self):
        try:
            logging.info("ineuron login function")
            #database connection
            self.__conn  = connect(user='root', password='subho@987', host = 'localhost', database = 'ineuron' )
            self._cursor = self.__conn.cursor()
        except Exception as e:
            logging.error(e)
    def user_authentication(self):
        try:
            logging.info("user sign up")

            user_choice = input("1.sign up \n2.sign in \nyour choice : ")
            
            if user_choice == "1":
                self.username = input("enter your  username for sign up : ")
                self.password = input("enter your password for sign up : ")
                self._cursor.execute("insert into user_authentication(username,password) values('%s','%s')"%(self.username,self.password))
                self.__conn.commit()
                print('succesfully inserted')
                self._cursor.close()
            if user_choice == '2':
                self.username = input("enter your  username for sign in : ")
                self.password = input("enter your password for sign in : ")
                self._cursor.execute("select * from user_authentication where username = '%s' and password = '%s'"%(self.username,self.password))
                print('ok')
                if self._cursor.fetchall():
                    print('%s is successfully logged in'%(self.username))
                    return 'ok'
                else:
                    print("login failed")
        except Exception as e:
            print(e)
            logging.error(e)

# x = oops_function()


'''ineuron course type choise'''
class course_type(oops_function):
    def __init__(self):
       x =  oops_function()
       result = x.user_authentication()
       if result == 'ok':
           print("*************************** welcome to ineuron ****************************************")
           top_category = input("1.couse \n2.internship \n3.job \n4.affiliates \n enter your choice : ")
           if top_category == '1':
               return 1
           elif top_category == '2':
               return 2
           if top_category == '3':
               return 3
           if top_category == '4':
               return 4
               # print('1.data science')
               # print('2.data analytics')
               # print('3.big data')
               # print('4.data engineering')
               # print('5.data management')
               # print('6.data warehouse')
                # print('7.data mining')





obj1 = course_type()
