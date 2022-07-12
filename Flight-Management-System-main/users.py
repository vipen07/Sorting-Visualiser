
# encapsulation
class users:
    def __init__(self, flight_manager):
        self.db = flight_manager
        self.db_cursor = flight_manager.cursor()


    def auth(self , username , password):
        sql_form = "select * from user where username = '{}' and password ='{}'".format(username , password)
        self.db_cursor.execute(sql_form)
        res = list(self.db_cursor)
        if res :
            return 1
        return 0

    def user_existance(self , username):
        sql_form = "SELECT * FROM user WHERE username = '{}'".format(username)
        self.db_cursor.execute(sql_form)
        res = list(self.db_cursor)
        if res:
            return 1
        return 0

    def checkadmin(self ,username):
        sql_form = "SELECT * FROM user WHERE username = '{}'".format(username)
        self.db_cursor.execute(sql_form)
        res = list(self.db_cursor)
        print(res[0][-1])

        if res[0][-1]==1:
            return 1
        return 0

    def add_user(self , username , name , age , password):
        if self.user_existance(username):
            print("USER ALREADY EXISTS")
            return


        sql_form = "Insert into user(username, name, age , password, isadmin) values(%s, %s, %s, %s, %s)"
        us = [(username ,name, age ,  password ,0 ) ,]
        self.db_cursor.executemany(sql_form, us)
        self.db.commit()
        print("User created Successfully !")
        return

    def show_tickets(self, username):
        sql_form = "select * from tickets where username ='{}'".format(username)
        self.db_cursor.execute(sql_form)
        res = list(self.db_cursor)
        if res :
            for i in range(len(res)):
                print(i + 1, *res[i])
        else :
            print("NO bookings yet")

    def search_flight(self , src , dest):
        sql_form = "Select * from flight   where  src = '{}' and dest='{}' order by  price".format(src, dest)
        self.db_cursor.execute(sql_form)
        res = list(self.db_cursor)
        if res:
            print("Top cheapest flights available for you !")
            for i in range(len(res)):
                print(i+1 , *res[i])
            print("Choose flight number  from above screen: ")
            n = int(input())
            if n>len(res) or n<1 :
                print("Invalid input")
            else :
                print("enter number of seats :")
                m = int(input())
                if res[n-1][-2]-m>=0:
                    print("Enter username")
                    username = input()
                    print("password")
                    password = input()
                    if(users.auth(self ,username ,password)):
                        #update seats
                        sql_form1 = "update flight set seat= '{}' where price = '{}' and src = '{}' and dest ='{}'".format(res[n-1][-2]-m , res[n-1][-1] ,
                                                                                                                             res[n-1][0] ,res[n-1][1])
                        self.db_cursor.execute(sql_form1)
                        self.db.commit()
                        #add ticket
                        sql_form2 = "insert into tickets values('{}' , '{}' , '{}' , '{}')".format(username , res[n-1][0] ,res[n-1][1], m)
                        self.db_cursor.execute(sql_form2)
                        self.db.commit()
                        print("Booking successful")
                    else :
                        print("invalid user credentials")
                else :
                    print("only '{}'  seats available".format(res[n-1][-1]))

        else:
            print("No flights available!")



class admins(users):

    #inheritance

    def __init__(self, flight_manager):
        super().__init__(flight_manager)
        self.db = flight_manager
        self.db_cursor = flight_manager.cursor()


    def delete_user(self, username):
        if users.user_existance(self , username):
            sql_form = "delete from user WHERE username='{}'".format(username)
            self.db_cursor.execute(sql_form)
            self.db.commit()
            print("USER DELETED SUCCESSFULLY !")
        else :
            print("USER DOESN'T EXISTS !")

    def make_admin(self ,username):
        if users.user_existance(self, username):
            sql_form = "update user set isadmin ='{}'  WHERE username='{}'".format(1 , username)
            self.db_cursor.execute(sql_form)
            self.db.commit()
            print("USER IS NOW ADMIN !")
        else:
            print("USER DOESN'T EXISTS !")

    def add_flights(self  , src ,dest ,  seats , price):
        sql_form = "Select * from flight where  src = '{}' and dest='{}' and price = '{}' ".format(src, dest ,price)
        self.db_cursor.execute(sql_form)
        res = list(self.db_cursor)
        if res:
            print("Flight already present")

        else :
            sql_form = "Insert into flight  values('{}', '{}', '{}', '{}')".format(src, dest, seats, price)
            # us = [(src , dest, price , seats),]
            self.db_cursor.execute(sql_form)
            self.db.commit()
            print("Flight added successfully")


