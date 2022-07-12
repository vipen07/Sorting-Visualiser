from dbms import give_user_admin


me, sup = give_user_admin()

while(1):
    print("                                ")
    print("WELCOME TO SUDHEER FLIGHT AGENCY")
    print("--------------------------------")
    print("1. BOOKING")
    print("2. MY BOOKINGS")
    print("3. SIGNUP")
    print("4. Admin Login")
    print("5. exit")
    print("choose your option")
    i = int(input())

    if i ==1 :
        print("enter source")
        src = input()
        print("enter dest")
        dest = input()
        print("Searching for flights from '{}' to '{}'".format(src , dest))
        me.search_flight(src , dest)

    if i==2 :
        print("Enter Username")
        username = input()
        print("Enter Password")
        password = input()
        if me.auth(username , password):
           me.show_tickets(username)
        else :
            print("INVALID CREDENTIALS")

    if i==3 :
        print("Enter Username ( this should be unique) :")
        username = input()
        print("Enter Password")
        password = input()
        print("Enter age")
        age = int(input())
        print("Enter Name")
        name = input()
        me.add_user(username , name, age, password)

    if i==4:
        print("Enter Username")
        username = input()
        print("Enter Password")
        password = input()
        if me.auth(username, password) and me.checkadmin(username):
            print("welcome admin")
            print("1 . add admin")
            print("2.  add flight")
            print("3 . delete user")
            j = int(input())
            if j==1 :
                print("enter  the existing username u want to be as an admin")
                username = input()
                sup.make_admin(username)

            if j==2 :
                print("enter source")
                src = input()
                print("enter dest")
                dest = input()
                print("enter seat")
                seat = int(input())
                print("enter price")
                price= int(input())
                sup.add_flights(src ,dest ,seat, price)

            if j==3 :
                print("enter username to be deleted")
                username=input()
                sup.delete_user(username)

        else :
            print("NOT AN ADMIN")
    if i==5:
        break
    else :
        print("enter valid option")

