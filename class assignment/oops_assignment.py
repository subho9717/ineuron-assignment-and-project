import logging
logging.basicConfig(filename='oops_assignment.log', level=logging.DEBUG,format='%(levelname)s %(asctime)s %(message)s')


class assignment1:
    def __init__(self):
        self.s = "this is My First Python programming class and i am learNING python string and its function"

        logging.info("sample data:"+':'+self.s)
    def q1(self):
        try:
            '''1 . Try to extract data from index one to index 300 with a jump of 3'''
            ans1 = self.s[1:300:3]
            logging.info("solution 1 " + '::' + ans1)
        except Exception as e:
            logging.error(e)


    def q2(self):
        try:
            '''2. Try to reverse a string without using reverse function'''
            ans2 = self.s[::-1]
            logging.info("solution 2 " + '::' + ans2)
        except Exception as e:
            logging.error(e)

    def q3(self):
        try:
            '''3. Try to split a string after conversion of entire string in uppercase'''
            ans3_1 = self.s.upper()
            ans3_2 = ans3_1.split()
            logging.info("solution 3 " + '::' + ans3_1)
            logging.info(ans3_2)
        except Exception as e:
            logging.error(e)

    def q4(self):
        try:
            '''4. try to convert the whole string into lower case'''
            ans4 = self.s.lower()
            logging.info("solution 4 " + '::' + ans4)
        except Exception as e:
            logging.error(e)

    def q5(self):
        try:
            '''5 . Try to capitalize the whole string'''
            ans5 = self.s.upper()
            logging.info("solution 5 " + '::' + ans5)
        except Exception as e:
            logging.error(e)

    def q6(self):
        try:
            '''6 . Write a diference between isalnum() and isalpha()'''
            ans5 = 'subho123'
            logging.info(ans5.isalnum())
            logging.info("solution 6 " + '::'+"isalnum() is use for find the numeric or alphabets  value in data")

            ans5_1 = 'subho'
            logging.info(ans5_1.isalpha())
            logging.info("solution 6 " + '::' + "ans5.isalpha() is usr for find the alphabets  value in data")
        except Exception as e:
            logging.error(e)

    def q7(self):
        try:
            '''7. Try to give an example of expand tab'''
            ans7 = "this\tis\texpand\ttab\texample"
            logging.info("solution 7 " + '::' + ans7)
        except Exception as e:
            logging.error(e)

    def q8(self):
        try:
            '''8 . Give an example of strip , lstrip and rstrip'''
            ans8 = "  example  "
            logging.info("solution 8 " + '::' + ans8.lstrip())
            logging.info("solution 8 " + '::' + ans8.rstrip())
        except Exception as e:
            logging.error(e)

    def q9(self):
        try:
            '''9.  Replace a string charecter by another charector by taking your own example'''
            ans9 = "example 1"
            logging.info("solution 8 " + '::' + ans9.replace('1','2'))
        except Exception as e:
            logging.error(e)

    def q10(self):
        try:
            '''10 . Try  to give a defination of string center function with and exmple'''
            ans10 = "example"
            logging.info(ans10.center(30,' '))
        except Exception as e:
            logging.error(e)

    def q11(self):
        try:
            '''11 . Write your own definition of compiler and interpretor without copy paste form internet in your own language'''
            ans10 = "example"
            logging.info("Ans 11 : python is a interpreater and compiler language.interpreter use to check the code line by line and compiler compile the code at once .In this method .py file compile to an intermediate code .pyc then this .pyc file  is directly interpreted as for final output" )
        except Exception as e:
            logging.error(e)

    def q12(self):
        try:
            '''13 . Try to write a usecase of python with your understanding .'''
            ans10 = "example"
            logging.info("Ans 11 : a)develop desktop software. "
                         "b)task automation.  "
                         "c) develop website. ")
        except Exception as e:
            logging.error(e)

class assignment2:

    def __init__(self):
        self.l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]

        """Task 2 
    
            l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
            1 . Try to reverse a list 
            2. try to access 234 out of this list 
            3 . try to access 456 
            4 . Try to extract only a list collection form list l 
            5 . Try to extract "sudh"
            6 . Try to list all the key in dict element avaible in list 
            7 . Try to extract all the value element form dict available in list"""
        logging.info(self.l)

    def q1(self):
        try:
            """1 . Try to reverse a list """
            logging.info(self.l[::-1])
        except Exception as e:
            logging.error(e)

    def q2(self):
        try:
            """2. try to access 234 out of this list """
            m1=self.l[7][0]
            m2 = list(self.l[8].keys())[1]
            # m = []
            # for r in self.l:
            #     if r == '234' :
            #         m.append(r)
            #     if type(r) == list:
            #         for i in r :
            #             if i == 234:
            #                 m.append(i)
            #
            #     if type(r) == tuple:
            #         for j in r :
            #             if j == 234:
            #                 m.append(j)
            #     if type(r) == dict:
            #         for k in r :
            #             if k == 234:
            #
            #                 m.append(k)
            logging.info([m1,m2])
        except Exception as e:
            logging.error(e)

    def q3(self):
        try:
            """3 . try to access 456"""
            logging.info(self.l[5][1])
        except Exception as e:
            logging.error(e)

    def q4(self):
        try:
            """4 . Try to extract only a list collection form list l """
            logging.info(self.l[5:7])
        except Exception as e:
            logging.error(e)

    def q5(self):
        try:
            """5 . Try to extract "sudh" """
            logging.info(list(self.l[8].values())[0])
        except Exception as e:
            logging.error(e)

    def q6(self):
        try:
            """6 . Try to list all the key in dict element avaible in list """
            logging.info(list(self.l[8].keys()))
        except Exception as e:
            logging.error(e)

    def q7(self):
        try:
            """7 . Try to extract all the value element form dict available in list"""
            logging.info(list(self.l[8].values()))
        except Exception as e:
            logging.error(e)

class assignment3:

    def __init__(self):
       self.l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
           {'k1': "sudh", "k2": "ineuron", "k3":"kumar", 3: 6, 7: 8}, ["ineuron", "data science "]]

        # '''q1 :
        # ineruon
        # ineruon ineruon
        # ineruon ineruon ineruon
        # ineruon ineruon ineruon ineruon
        #
        # q2 -
        #
        #           ineruon
        #     ineruon      ineruon
        # ineruon		ineruon 	ineruon
        #     ineruon		 ineruon
        #           ineruon
        #
        # l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
        #             "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
        #
        # q3 : Try to extract all the list entity
        # q4 : Try to extract all the dict enteties
        # q5 : Try to extract all the tuples entities
        # q6 : Try to extract all the numerical data it may b a part of dict key and values
        # q7 : Try to give summation of all the numeric data
        # q8 : Try to filter out all the odd values out all numeric data which is a part of a list
        # q9 : Try to extract "ineruon" out of this data
        # q10 : Try to find out a number of occurances of all the data
        # q11 : Try to find out number of keys in dict element
        # q12 : Try to filter out all the string data
        # q13 : Try to Find  out alphanum in data
        # q14 : Try to find out multiplication of all numeric value in the individual collection inside dataset'''
    def q1(self):
        try:
            """q1 :
            ineruon
            ineruon ineruon
            ineruon ineruon ineruon
            ineruon ineruon ineruon ineruon"""

            x = 5
            # for i in range(x):
            #     for j in range(i):
            #         print('ineruon',end=" ")
            #     print('')
            for i in range(x):
                print(' ineruon '*(i+1))
            logging.info('ok')
        except Exception as e:
            logging.error(e)

    def q2(self):
        try:
            for i in range(6):
                if i <= 3:
                    n = i
                else:
                    n = 6 - i
                print(("ineuron "*n).center(30,' '))

            logging.info('ok')
        except Exception as e:
            logging.error(e)

    def q3(self):
        try:
            """q3 : Try to extract all the list entity"""


            for i in self.l:
                if type(i) == list:
                    print(i)
            logging.info('ok')
        except Exception as e:
            logging.error(e)

    def q4(self):
        try:
            """q4 : Try to extract all the dict enteties"""

            for i in self.l:
                if type(i) == dict:
                    print(i)
            logging.info('ok')
        except Exception as e:
            logging.error(e)

    def q5(self):
        try:
            """q5 : Try to extract all the tuples entities"""

            for i in self.l:
                if type(i) == tuple:
                    print(i)
            logging.info('ok')
        except Exception as e:
            logging.error(e)

    def q6(self):
        try:
            """q6 : Try to extract all the numerical data it may b a part of dict key and values"""
            self.li = []
            for i in self.l:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for t in i:
                      if type(t)  == int:
                            self.li.append(t)
                if type(i) == dict:
                    for d in i.items():
                        if type(d[0]) ==int:
                            self.li.append(d[0])
                        if type(d[1]) == int:
                            self.li.append(d[1])
            logging.info(self.li)
        except Exception as e:
            logging.error(e)

    def q7(self):
        try:
            """q7 : Try to give summation of all the numeric data"""

            s = sum(self.li)
            logging.info(s)
        except Exception as e:
            logging.error(e)

    def q8(self):
        try:
            """q8 : Try to filter out all the odd values out all numeric data which is a part of a list"""

            self.li = []
            for i in self.l:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for t in i:
                        if type(t) == int:
                            if t %2!=0:
                                self.li.append(t)
            logging.info(self.li)
        except Exception as e:
            logging.error(e)

    def q9(self):
        try:
            """q9 : Try to extract "ineruon" out of this data"""


            self.li1 = []
            for i in self.l:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for t in i:
                        if t == 'ineuron':
                            self.li1.append(t)
                if type(i) == dict:
                    for d in i.items():
                        if d[0] == 'ineuron':
                            self.li1.append(d[0])
                        if d[1] == 'ineuron':
                            self.li1.append(d[1])
            logging.info(self.li1)
        except Exception as e:
            logging.error(e)

    def q10(self):
        try:
            """q10 : Try to find out a number of occurances of all the data"""


            li2 = []
            for i in self.l:
                if type(i) == tuple or type(i) == list or type(i) == set or  type(i) == str:
                    for t in i:
                        if type(t) == str or type(t) == int:
                            li2.append(t)
                if type(i) == dict:
                    for d in i.items():
                        for g in d:
                            if type(g) == str or type(g) == int:
                                li2.append(g)

            print(li2)
            logging.info(li2)
        except Exception as e:
            logging.error(e)

    def q11(self):
        try:
            """q11 : Try to find out number of keys in dict element"""


            li2 = []
            for i in self.l:
                if type(i) == dict:
                    for d in i.items():
                        li2.append(d[0])
                        # print(d[0])
                                
            # print(len(li2))
            logging.info("dictionary key length id : "+len(li2))
        except Exception as e:
            logging.error(e)

    def q12(self):
        try:
            """q12 : Try to filter out all the string data"""


            self.li2 = []
            for i in self.l:
                if type(i) == tuple or type(i) == list or type(i) == set or  type(i) == str:
                    for t in i:
                        if type(t) == str:
                            self.li2.append(t)
                if type(i) == dict:
                    for d in i.items():
                        for g in d:
                            if type(g) == str :
                                self.li2.append(g)

            # print(self.li2)
            logging.info("str data : "+len(self.li2))
        except Exception as e:
            logging.error(e)

    def q13(self):
        try:
            """q13 : Try to Find  out alphanum in data"""


            li2 = []
            for i in self.li2:
                if i.isalnum():
                    li2.append(i)
            print(li2)

            
            logging.info("str data : "+len(li2))
        except Exception as e:
            logging.error(e)

    def q14(self):
        try:
            self.li = []
            for i in self.l:
                n=1

                if type(i) == tuple or type(i) == list or type(i) == set:
                    for t in i:
                      if type(t)  == int:
                        n=t*n
                    # print(n)
                    self.li.append(n)
                if type(i) == dict:
                    for d in i.items():
                        for k in d:
                            if type(k) == int:
                                n=k*n
                        
                    self.li.append(d[1])
            print(self.li)
            logging.info(self.li)
        except Exception as e:
            logging.error(e)

class assignment4:

    def __init__(self):
       '''q1 : Try to print this by using while loop 
        * 
        * * 
        * * * 
        * * * * 
        * * * * * 
        * * * * * * 
        * * * * * * * 
        * * * * * * * * 
        * * * * * * * * * 

        q2 : try to print below by using while loop : 
                
        A
        B H 
        C I N
        D J o S
        E K p T W
        F L Q U X z
        G M R V Y 

        q3 : Try to print all the number divisible by 3 in between a range of 40 - 400
            
        q4 : Try to filter out all the vowels form below text by using while loop : 
        """Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]

        Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]

        Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36]

        Python consistently ranks as one of the most popular programming languagesc""" 


        q5 : Try to generate all the even number between 1- 1000

        q6 : Define a function for all the above problem statememnt  . 
            
        q7 : write a code to get a time of your system 

        q8 : Write a code to fetch date form your system 

        q9 : Write a code to send a mail to your friend 

        q10 : write a code to trigger alarm for you at scheduled time 

        q11 : write a code to check ip address of your system 

        q12 : Write a code to check a perticular installation in your system

        q13 : Write a code to convert any text in to voice 

        q14 : you have to write a fun which will take string and return a len of 
        it without using a inbuilt fun len

        q15 :write a fun which will be able to print an index of all premitive element which you will pass 

        q16 : Write a fun which will take input as a dict and give me out as a list of all the values 
        even in case of 2 level nesting it should work . 

        q17 : write a function whihc will take multiple list as a input and give me concatnation of all the element as 
        and output

        q18 : Write a function which will whould return list of all the file name from a directory . 

        q19 : write a function whihc will be able to read a image file and show it to you .
            
        q20 : write a function by which you will be able to append two PDF files . 
            
        q21 : write a function which can help you to filter only word file from a directory . 
            
        q22 : write a function which can read video file and play for you . 
            
        q23 : write a function which will be able to shutdonw your system . 

        q24 : Write a function which will whould return list of all the file name from a directory . 

        q25 : write a function whihc will be able to access your mail . '''

    def q1(self):
        try:
            '''q1 : Try to print this by using while loop 
        * 
        * * 
        * * * 
        * * * * 
        * * * * * 
        * * * * * * 
        * * * * * * * 
        * * * * * * * * 
        * * * * * * * * * '''
            
            i = 1
            k = 10
            while i <= k:#row
                print(" * " * i)   
                i = i + 1
        except Exception as e:
            logging.error(e)

    # def q2(self):
    #     try:
    #         '''q2 : try to print below by using while loop :
    #
    #     A
    #     B H
    #     C I N
    #     D J o S
    #     E K p T W
    #     F L Q U X z
    #     G M R V Y '''
    #         i = 1
    #         k = 10
    #         while i <= k:#row
    #             print()
    #
    #             i = i + 1
    #     except Exception as e:
    #         logging.error(e)

# as1.q1()
# as1.q2()
# as1.q3()
# as1.q4()
# as1.q5()
# as1.q6()
# as1.q7()
# as1.q8()
# as1.q9()
# as1.q10()
# as1.q11()
# as1.q12()

as2 = assignment2()
# as2.q1()
# as2.q2()
# as2.q3()
# as2.q4()
# as2.q5()
# as2.q6()
# as2.q7()

as3 = assignment3()
# as3.q1()
# as3.q2()
# as3.q3()
# as3.q4()
# as3.q5()
# as3.q6()
# as3.q7()
# as3.q8()
# as3.q9()
# as3.q10()
# as3.q11()
# as3.q12()
# as3.q13()
# as3.q14()

as3 = assignment4()
# as3.q1()
as3.q2()