# ORM with get, all, filter, save and create functionality:

import sqlite3
import pudb
import sys

connection = sqlite3.connect('babyorm.db')
c = connection.cursor()

class Model:
    def __init__(self, **kwargs):
        # for i in kwargs.keys():
        for key,value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def all(cls):
        table_name = cls.__name__
        print ("")
        print ("Table:", table_name)
        table = c.execute(
            """
            SELECT * FROM {};
            """.format(table_name))
        connection.commit()
        full_table = (table.fetchall())
        length = (len(full_table))
        for row in range (0,length):
            print (full_table[row])

    @classmethod
    def get(cls, **kwargs):
        table_name = cls.__name__
        print ("")
        print ("In table:", table_name)
        for key,value in kwargs.items():
            condition = key
            length = (len(value))
            for i in range (0,length):
                given_value = value [i]
                print("Your condition is: {x}, with a value of: {y}".format(x = condition, y = given_value))
                try:
                    row = c.execute(
                        """
                        SELECT * FROM {} WHERE {} = "{}"
                        """.format(table_name, condition, given_value))
                    connection.commit()
                except:
                    print ("-- This is an invalid search --")
                    break
                "This returns one result, the first one."
                print ("One result:")
                result = (row.fetchone())
                print (result)
                print ("")

    @classmethod
    def filter(cls, **kwargs):
        table_name = cls.__name__
        print ("")
        print ("In table:", table_name)
        for key,value in kwargs.items():
            condition = key
            value = value
            print("Your condition is: {x}, with a value of: {y}".format(x = key, y = value))
            try:
                row = c.execute(
                    """
                    SELECT * FROM {} WHERE {} = "{}"
                    """.format(table_name, condition, value))
                connection.commit()
            except:
                print ("-- This is an invalid search --")
                break
            "This returns many results, all that meet the criteria."
            results = (row.fetchall())
            length = (len(results))
            print ("All results:")
            for row in range (0,length):
                print (results[row])
            print ("")

    @classmethod
    def save(cls, **kwargs):
        table_name = cls.__name__
        print ("")
        print ("In table:", table_name)
        # need to be in one loop bc they are unordered
        key_statement = ""
        value_statement = ""
        for key in kwargs.keys():
            # create a string of all the columns
            key_statement += "{},".format(key)
            # create a list of all the values         
            value_statement += '"{}",'.format(kwargs[key])
            # check all the columns are in the db - ?!

        value_statement = value_statement[:-1]
        key_statement = key_statement[:-1]
        print("Your column names are: -- {x} -- , and you are setting them with values of: -- {y} -- ".format(x = key_statement, y = value_statement))
        # pass these lists into the SQL with the right format
        try:
            c.execute("""
            INSERT INTO {x} ({y}) VALUES ({z});
            """.format(x=table_name, y=key_statement, z=value_statement) #,(value_statement,)
            )
            connection.commit()
            print ("...processing...")
            print ("Updated the database acourdingly.")
        except:
            print ("")
            print ("INSERT FAILED")
            print ("-- This is an invalid input --")
       
    # @classmethod
    # def saveT(cls):
    #     table_name = cls.__name__
    #     conn= sqlite3.connect("babyorm.db")
    #     c = conn.cursor()
    #     c.execute("""PRAGMA table_info({})""".format(table_name))
    #     result = c.fetchall()
    #     print('Table info---',len(result))

# don't touch the code for these
class Users(Model):
    pass

class Stocks(Model):
    pass

# stock = Stocks()
# stock.all()

user = Users(name="jack", username = "Janteby", emial = "Janteby1@gmail.com")
# print ("added user:", user.name, user.username)
user.all()

test = {"health":["Dr.", "Elodie"]}
user.get(**test)

tests = {"name":"jack","ID":"22."}
user.filter(**tests)

user.save(name="bary", username="final", email="there@usa.com")
user.all() # check if the new user got added 




"New syntax: keeps your program running even if it hits an error, like a conditional"
# try:
#     # something 
# except:
#     # give a message if fails
# else:
#     # final error 



'''
Table: Stocks
(1, 'LZH', 69.21)
(2, 'FZ', 354.23)
(3, 'UKQ', 214.44)
(4, 'PQMS', 276.13)
(5, 'QTZX', 217.84)
(6, 'XWN', 117.06)
(7, 'DFIL', 282.99)
(8, 'XQ', 88.14)
(9, 'UNZ', 151.42)
(10, 'VYO', 109.12)
(11, 'GJC', 137.44)
(12, 'EJY', 95.84)
(13, 'SWUX', 252.12)
(14, 'IJ', 221.69)
(15, 'QHL', 213.55)
(16, 'LDAQ', 12.53)
(17, 'JGLU', 244.02)
(18, 'GWZI', 84.76)
(19, 'LEO', 313.7)
(20, 'XE', 254.2)
(21, 'XBF', 24.08)
(22, 'DALV', 93.01)
(23, 'EHM', 343.09)
(24, 'KTFA', 181.88)
(25, 'YRX', 226.84)

Table: Users
(1, 'Dr.', '704 Lesley Square Apt. 194\nWest Belvaton, NE 67304', 35969.0)
(2, 'Harlan', '2242 Jordan Ranch\nEast Roseanne, WI 32166', 14957.0)
(3, 'Sterling', '11581 Reginald Park\nPort Maddoxview, ME 60969', 85716.0)
(4, 'Cilla', 'PSC 2154, Box 8541\nAPO AA 21813-9475', 73842.0)
(5, 'Roseann', '6507 Alzina Locks\nAlisonton, MS 86939-2721', 53452.0)
(6, 'Marcia', '63253 Lynch Rapid Apt. 004\nNew Claudettestad, LA 81577-8194', 55100.0)
(7, 'Carri', '9797 Steuber Forks Apt. 732\nLake Monroefurt, CA 41689', 99222.0)
(8, 'Dr.', '09031 Dooley Stravenue\nWest Mychal, SC 44468', 71609.0)
(9, 'Mr.', '15979 Boyer Rest Apt. 779\nRobertsfort, NY 97574-2489', 55479.0)
(10, 'Lessie', '945 Flatley Landing\nWest Amiahfort, NC 09484', 21020.0)
(11, 'Cinnamon', '13914 Willms Meadows Suite 021\nFayburgh, WV 34785-8323', 61947.0)
(12, 'Martha', '586 Mitchell Brooks\nMegganmouth, ME 38411', 52163.0)
(13, 'Sandra', '139 Emmons Point Apt. 857\nLorahaven, KS 85030-8151', 3365.0)
(14, 'Edwina', '21219 Susie Cape\nJohnstonview, FM 42784', 83548.0)
(15, 'Dr.', '705 Carin Crossing\nNorth Wm, OK 64294-2795', 39994.0)
(16, 'Dr.', 'USS Parisian\nFPO AP 19595', 80923.0)
(17, 'Adrienne', '9645 Grover Trafficway Apt. 440\nTeenaborough, MI 46866', 70332.0)
(18, 'Kenny', '63603 McCullough Mission\nAbshire, OR 26034-9865', 3706.0)
(19, 'Portia', '2619 Coy Avenue Apt. 687\nTheaview, WY 29631-5203', 85247.0)
(20, 'Braydon', '76438 Kamari Park\nWest Martha, RI 50583-2629', 36740.0)
(21, 'Geoff', '2950 Frami Harbors\nWiltonfurt, IA 83745-3427', 68677.0)
(22, 'Elodie', '16721 Prosacco Landing\nNew Yvonne, HI 25564', 38731.0)
(23, 'Dwayne', 'PSC 9939, Box 2737\nAPO AE 52071', 13232.0)
(24, 'Myles', 'Unit 3263 Box 7113\nDPO AA 89924', 74939.0)
(25, 'Judie', '217 Nicolas Lock\nTerrellmouth, MD 96599-0624', 72896.0)

In table: Users
Your condition is: name, with a value of: Dr.
One result:
(1, 'Dr.', '704 Lesley Square Apt. 194\nWest Belvaton, NE 67304', 35969.0)

In table: Users
Your condition is: name, with a value of: Dr.
All results:
(1, 'Dr.', '704 Lesley Square Apt. 194\nWest Belvaton, NE 67304', 35969.0)
(8, 'Dr.', '09031 Dooley Stravenue\nWest Mychal, SC 44468', 71609.0)
(15, 'Dr.', '705 Carin Crossing\nNorth Wm, OK 64294-2795', 39994.0)
(16, 'Dr.', 'USS Parisian\nFPO AP 19595', 80923.0)




In table: Users
Your condition is: name, with a value of: Dr.
One result:
(1, 'Dr.', '704 Lesley Square Apt. 194\nWest Belvaton, NE 67304', 35969.0)

Your condition is: name, with a value of: Elodie
One result:
(22, 'Elodie', '16721 Prosacco Landing\nNew Yvonne, HI 25564', 38731.0)


In table: Users
Your condition is: name, with a value of: Dr.
All results:
(1, 'Dr.', '704 Lesley Square Apt. 194\nWest Belvaton, NE 67304', 35969.0)
(8, 'Dr.', '09031 Dooley Stravenue\nWest Mychal, SC 44468', 71609.0)
(15, 'Dr.', '705 Carin Crossing\nNorth Wm, OK 64294-2795', 39994.0)
(16, 'Dr.', 'USS Parisian\nFPO AP 19595', 80923.0)

Your condition is: ID, with a value of: 22.
All results:
(22, 'Elodie', '16721 Prosacco Landing\nNew Yvonne, HI 25564', 38731.0)




Table: Users
(1, 'test', 'testing', 'testing@gmail.com', None, None)
(2, 'Jack', 'Janteby', 'Janteby@gmail.com', None, None)
(3, 'test2', 'testing2', 'testing2@gmail.com', None, None)
(4, 'bary', 'final', 'there@usa.com', None, None)

In table: Users
Your condition is: health, with a value of: Dr.
-- This is an invalid search --

In table: Users
Your condition is: name, with a value of: jack
All results:

Your condition is: ID, with a value of: 22.
All results:


In table: Users
Your column names are: -- email,name,username -- , and you are setting them with values of: -- "there@usa.com","bary","final" -- 
...processing...
Updated the database acourdingly.

Table: Users
(1, 'test', 'testing', 'testing@gmail.com', None, None)
(2, 'Jack', 'Janteby', 'Janteby@gmail.com', None, None)
(3, 'test2', 'testing2', 'testing2@gmail.com', None, None)
(4, 'bary', 'final', 'there@usa.com', None, None)
(5, 'bary', 'final', 'there@usa.com', None, None)
Jacks-MacBook-Pro-2:baby_orm_save JackAAnteby$ 

'''



