import mysql.connector
import  users

#connecting to our database using python
flight_manager = mysql.connector.connect(
    host="localhost",
    user="root",
    port='3306',
    password="VipendraS-07r",
    database='flight-management-system',
)
if flight_manager.is_connected():
    print("successfully connected")
#cursor for traversing in the database


my_cursor = flight_manager.cursor()


#passing user and admin objects

def give_user_admin():
    user = users.users(flight_manager)
    admin = users.admins(flight_manager)

    me =user
    sup = admin
    return [me, sup]
