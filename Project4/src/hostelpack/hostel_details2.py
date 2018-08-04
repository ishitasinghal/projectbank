class H:
    def select(self,name,about,rooms,transport,price,facilities,book_now,n):
        self.name=name
        self.about=about
        self.rooms=rooms
        self.transport=transport
        self.price=price
        self.facilities=facilities
        self.book_now=book_now
        a=10
        while(a!=0):
            print("----------",self.name,"--------------")
            print("1.About")
            print("2.Rooms")
            print("3.Transport")
            print("4.Facilities")
            print("5.Price")
            print("6.Book now")
            print("7.Student login")
            print("8.Staff login")
            print("Press 0 to exit")
            
        
            a=int(input("Enter your choice number(options):"))
            print("\n")
            if(a<0 or a>8):
                print("-->>Wrong choice; Enter your choice again\n")
            if(a==1):
                print(self.about)
            if(a==2):
                print(self.rooms)
            if(a==3):
                print(self.transport)
            if(a==4):
                print(self.facilities)
            if(a==5):
                print(self.price)
            if(a==6):
                print(self.book_now)
            if(a==7):
                import sys
                import cx_Oracle
                con=cx_Oracle.connect('SYSTEM/user1@localhost/xe')
                cur=con.cursor()
                user=input("Enter your username:")
                if(n==1):
                    cur.execute("select STUSER_ID from stuid1")
                    t=cur.fetchall()
                    c=0
                    for i in t:
                        x=i[0]
                        if(x==user):
                            c=1
                            p=0
                            while(p!=1):
                                password=input("Enter password:")
                                cur.execute("select STU_pswd from stuid1")
                                r=cur.fetchall()
                                for j in r:
                                    y=j[0]
                                    
                                    if(y==password):
                                        p=1
                                        cur.execute("select * from stu_details1 where stuser_id = :n", {'n':user})
                                        print("\n***************DETAILS*****************")
                                        z=('Student id: ', 'Name: ', 'Room no: ')
                                        print(z)
                                        print(cur.fetchall())
                                        cur.execute("select days_present from stu_attendance1 where stu_id = :m", {'m':user})
                                        print("No. of days present: ",cur.fetchall() )
                                        print("****************************************\n")
                                if(p!=1):
                                    q=int(input("Wrong password; press 1 to enter again or press 0 to exit "))
                                    if(q==0):
                                        print("-------------------------------------------------------------")
                                        print("You may run the whole program again if you want to know more")
                                        print("                        Thank You                           ")
                                        sys.exit()
                            
                    if(c!=1):
                        print("You are not enrolled or the user id you entered is incorrect. ")
                if(n==2):
                    cur.execute("select STUSER_ID from stuid2")
                    t=cur.fetchall()
                    c=0
                    for i in t:
                        x=i[0]
                        if(x==user):
                            c=1
                            p=0
                            while(p!=1):
                                password=input("Enter password:")
                                cur.execute("select STU_pswd from stuid2")
                                r=cur.fetchall()
                                for j in r:
                                    y=j[0]
                                    
                                    if(y==password):
                                        p=1
                                        cur.execute("select * from stu_details2 where stuser_id = :n", {'n':user})
                                        print("\n***************DETAILS*****************")
                                        z=('Student id: ', 'Name: ', 'Room no: ')
                                        print(z)
                                        print(cur.fetchall())
                                        cur.execute("select days_present from stu_attendance2 where stu_id = :m", {'m':user})
                                        print("No. of days present: ",cur.fetchall() )
                                        print("****************************************\n")
                                if(p!=1):
                                    q=int(input("Wrong password; press 1 to enter again or press 0 to exit "))
                                    if(q==0):
                                        print("-------------------------------------------------------------")
                                        print("You may run the whole program again if you want to know more")
                                        print("                        Thank You                           ")
                                        sys.exit()
                            
                    if(c!=1):
                        print("You are not enrolled or the user id you entered is incorrect. ")
                if(n==3):
                    cur.execute("select STUSER_ID from stuid3")
                    t=cur.fetchall()
                    c=0
                    for i in t:
                        x=i[0]
                        if(x==user):
                            c=1
                            p=0
                            while(p!=1):
                                password=input("Enter password:")
                                cur.execute("select STU_pswd from stuid3")
                                r=cur.fetchall()
                                for j in r:
                                    y=j[0]
                                    
                                    if(y==password):
                                        p=1
                                        cur.execute("select * from stu_details3 where stuser_id = :n", {'n':user})
                                        print("\n***************DETAILS*****************")
                                        z=('Student id: ', 'Name: ', 'Room no: ')
                                        print(z)
                                        print(cur.fetchall())
                                        cur.execute("select days_present from stu_attendance3 where stu_id = :m", {'m':user})
                                        print("No. of days present: ",cur.fetchall() )
                                        print("****************************************\n")
                                if(p!=1):
                                    q=int(input("Wrong password; press 1 to enter again or press 0 to exit "))
                                    if(q==0):
                                        print("-------------------------------------------------------------")
                                        print("You may run the whole program again if you want to know more")
                                        print("                        Thank You                           ")
                                        sys.exit()
                            
                    if(c!=1):
                        print("You are not enrolled or the user id you entered is incorrect. ")
                if(n==4):
                    cur.execute("select STUSER_ID from stuid4")
                    t=cur.fetchall()
                    c=0
                    for i in t:
                        x=i[0]
                        if(x==user):
                            c=1
                            p=0
                            while(p!=1):
                                password=input("Enter password:")
                                cur.execute("select STU_pswd from stuid4")
                                r=cur.fetchall()
                                for j in r:
                                    y=j[0]
                                    
                                    if(y==password):
                                        p=1
                                        cur.execute("select * from stu_details4 where stuser_id = :n", {'n':user})
                                        print("\n***************DETAILS*****************")
                                        z=('Student id: ', 'Name: ', 'Room no: ')
                                        print(z)
                                        print(cur.fetchall())
                                        cur.execute("select days_present from stu_attendance4 where stu_id = :m", {'m':user})
                                        print("No. of days present: ",cur.fetchall() )
                                        print("****************************************\n")
                                if(p!=1):
                                    q=int(input("Wrong password; press 1 to enter again or press 0 to exit "))
                                    if(q==0):
                                        print("-------------------------------------------------------------")
                                        print("You may run the whole program again if you want to know more")
                                        print("                        Thank You                           ")
                                        sys.exit()
                            
                    if(c!=1):
                        print("You are not enrolled or the user id you entered is incorrect. ")
                if(n==5):
                    cur.execute("select STUSER_ID from stuid5")
                    t=cur.fetchall()
                    c=0
                    for i in t:
                        x=i[0]
                        if(x==user):
                            c=1
                            p=0
                            while(p!=1):
                                password=input("Enter password:")
                                cur.execute("select STU_pswd from stuid5")
                                r=cur.fetchall()
                                for j in r:
                                    y=j[0]
                                    
                                    if(y==password):
                                        p=1
                                        cur.execute("select * from stu_details5 where stuser_id = :n", {'n':user})
                                        print("\n***************DETAILS*****************")
                                        z=('Student id: ', 'Name: ', 'Room no: ')
                                        print(z)
                                        print(cur.fetchall())
                                        cur.execute("select days_present from stu_attendance5 where stu_id = :m", {'m':user})
                                        print("No. of days present: ",cur.fetchall() )
                                        print("****************************************\n")
                                if(p!=1):
                                    q=int(input("Wrong password; press 1 to enter again or press 0 to exit "))
                                    if(q==0):
                                        print("-------------------------------------------------------------")
                                        print("You may run the whole program again if you want to know more")
                                        print("                        Thank You                           ")
                                        sys.exit()
                            
                    if(c!=1):
                        print("You are not enrolled or the user id you entered is incorrect. ")    
    

    
                con.close()
            
class v_g(H):
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        n=1
        #Hostel.select(self,name,about,rooms,transport,price,facilities,book_now)
        super().select(name,about,rooms,transport,price,facilities,book_now,n)
        #def s_login_info(self):
        
class v_b(H):
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        n=2
        #Hostel.select(self,name,about,rooms,transport,price,facilities,book_now)
        super().select(name,about,rooms,transport,price,facilities,book_now,n)
class a(H):
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        n=3
        #Hostel.select(self,name,about,rooms,transport,price,facilities,book_now)
        super().select(name,about,rooms,transport,price,facilities,book_now,n)
class s(H):
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        n=4
        #Hostel.select(self,name,about,rooms,transport,price,facilities,book_now)
        super().select(name,about,rooms,transport,price,facilities,book_now,n)
class p(H):
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        n=5
        #Hostel.select(self,name,about,rooms,transport,price,facilities,book_now)
        super().select(name,about,rooms,transport,price,facilities,book_now,n)

obj1= v_g()
obj2=v_b()
obj3=a()
obj4=s()
obj5=p()


