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
        ocpd = 0
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
                print("Total vacancy: 50")
                vacant = 50-ocpd
                print("Vacancy left: " ,vacant)
                if(ocpd == 50):
                    print("Sorry!!1 No rooms left")
                else:
                    print("Enter details of the student")
                    name = input("Enter your name:")
                    stuid = int(input("Enter your id:"))
                    pswd = input("Enter password of atleast more than 6 characters")
                    while(len(pswd)<6):
                        print("Invalid password !! try again")
                        pswd=input("Enter password again")
                    npswd=input("Enter password again")
                    if(npswd==pswd):
                        print("Password set successfully!!!")
                        print("Visit www.abc.com for payment options")
                        room_no = str(0)+str(ocpd)
                        import cx_Oracle
                        con=cx_Oracle.connect('SYSTEM/user1@localhost/xe')
                        cur=con.cursor()
                        if(n==1):
                            #cur.execute("drop table stuid11")
                            #cur.execute("create table stuid11(STUSER_ID VARCHAR(30) primary key not null,STU_PSWD VARCHAR(15) not null check(length(stu_pswd)>6))") 
                            cur.execute("insert into stuid11 values(:a,:b)",(stuid,pswd))
                            con.commit()
                            #cur.execute("drop table stu_details11")
                            #cur.execute('''CREATE TABLE stu_details11(STUSER_ID VARCHAR(30),STU_NAME VARCHAR(30), STU_ROOMNO INTEGER, foreign key(stuser_id) references stuid11(stuser_id))''')
                            cur.execute("insert into stu_details11 values(:a,:b,:c)",(stuid,name,room_no))
                            con.commit()
                            print("Congratulations!!!!! your room has been booked!!")
                            print("Your room number is : " , room_no)
                            ocpd=ocpd+1
                        elif(n==2):
                            cur.execute("drop table stuid22")
                            cur.execute("create table stuid22(STUSER_ID VARCHAR(30) primary key not null,STU_PSWD VARCHAR(15) not null check(length(stu_pswd)>6))") 
                            cur.execute("insert into stuid22 values(:a,:b)",(stuid,pswd))
                            con.commit()
                            cur.execute("drop table stu_details22")
                            cur.execute('''CREATE TABLE stu_details22(STUSER_ID VARCHAR(30),STU_NAME VARCHAR(30), STU_ROOMNO INTEGER, foreign key(stuser_id) references stuid11(stuser_id))''')
                            cur.execute("insert into stu_details22 values(:a,:b,:c)",(stuid,name,room_no))
                            con.commit()
                            print("Congratulations!!!!! your room has been booked!!")
                            print("Your room number is : " , room_no)
                            ocpd=ocpd+1
                        elif(n==3):
                            #cur.execute("drop table stuid33")
                            cur.execute("create table stuid33(STUSER_ID VARCHAR(30) primary key not null,STU_PSWD VARCHAR(15) not null check(length(stu_pswd)>6))") 
                            cur.execute("insert into stuid33 values(:a,:b)",(stuid,pswd))
                            con.commit()
                            #cur.execute("drop table stu_details33")
                            cur.execute('''CREATE TABLE stu_details33(STUSER_ID VARCHAR(30),STU_NAME VARCHAR(30), STU_ROOMNO INTEGER, foreign key(stuser_id) references stuid11(stuser_id))''')
                            cur.execute("insert into stu_details33 values(:a,:b,:c)",(stuid,name,room_no))
                            con.commit()
                            print("Congratulations!!!!! your room has been booked!!")
                            print("Your room number is : " , room_no)
                            ocpd=ocpd+1
                        elif(n==4):
                            cur.execute("drop table stuid44")
                            cur.execute("create table stuid44(STUSER_ID VARCHAR(30) primary key not null,STU_PSWD VARCHAR(15) not null check(length(stu_pswd)>6))") 
                            cur.execute("insert into stuid44 values(:a,:b)",(stuid,pswd))
                            con.commit()
                            cur.execute("drop table stu_details44")
                            cur.execute('''CREATE TABLE stu_details44(STUSER_ID VARCHAR(30),STU_NAME VARCHAR(30), STU_ROOMNO INTEGER, foreign key(stuser_id) references stuid11(stuser_id))''')
                            cur.execute("insert into stu_details44 values(:a,:b,:c)",(stuid,name,room_no))
                            con.commit()
                            print("Congratulations!!!!! your room has been booked!!")
                            print("Your room number is : " , room_no)
                            ocpd=ocpd+1
                        elif(n==5):
                            cur.execute("drop table stuid55")
                            cur.execute("create table stuid55(STUSER_ID VARCHAR(30) primary key not null,STU_PSWD VARCHAR(15) not null check(length(stu_pswd)>6))") 
                            cur.execute("insert into stuid55 values(:a,:b)",(stuid,pswd))
                            con.commit()
                            cur.execute("drop table stu_details55")
                            cur.execute('''CREATE TABLE stu_details55(STUSER_ID VARCHAR(30),STU_NAME VARCHAR(30), STU_ROOMNO INTEGER, foreign key(stuser_id) references stuid11(stuser_id))''')
                            cur.execute("insert into stu_details55 values(:a,:b,:c)",(stuid,name,room_no))
                            con.commit()
                            print("Congratulations!!!!! your room has been booked!!")
                            print("Your room number is : " , room_no)
                            ocpd=ocpd+1
                    else:
                        while(npswd is not pswd):
                            npswd=input("Password didn't match,enter again")
                                
                                
                    
            if(a==7):
                import sys
                con=cx_Oracle.connect('SYSTEM/user1@localhost/xe')
                cur=con.cursor()
                user=input("Enter your user id:")
                if(n==1):
                    cur.execute("select STUSER_ID from stuid11")
                    t=cur.fetchall()
                    c=0
                    for i in t:
                        x=i[0]
                        if(x==user):
                            c=1
                            p=0
                            while(p!=1):
                                password=input("Enter password:")
                                cur.execute("select STU_pswd from stuid11")
                                r=cur.fetchall()
                                for j in r:
                                    y=j[0]
                                    
                                    if(y==password):
                                        p=1
                                        cur.execute("select * from stu_details11 where stuser_id = :n", {'n':user})
                                        print("\n***************DETAILS*****************")
                                        z=('Student id: ', 'Name: ', 'Room no: ')
                                        print(z)
                                        print(cur.fetchall())
                                        #cur.execute("select days_present from stu_attendance11 where stu_id = :m", {'m':user})
                                        #print("No. of days present: ",cur.fetchall() )
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
                    con.close()    
                if(n==3):
                    cur.execute("select STUSER_ID from stuid33")
                    t=cur.fetchall()
                    c=0
                    for i in t:
                        x=i[0]
                        if(x==user):
                            c=1
                            p=0
                            while(p!=1):
                                password=input("Enter password:")
                                cur.execute("select STU_pswd from stuid33")
                                r=cur.fetchall()
                                for j in r:
                                    y=j[0]
                                    
                                    if(y==password):
                                        p=1
                                        cur.execute("select * from stu_details33 where stuser_id = :n", {'n':user})
                                        print("\n***************DETAILS*****************")
                                        z=('Student id: ', 'Name: ', 'Room no: ')
                                        print(z)
                                        print(cur.fetchall())
                                        cur.execute("select days_present from stu_attendance33 where stu_id = :m", {'m':user})
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
                if(n==4):
                    cur.execute("select STUSER_ID from stuid44")
                    t=cur.fetchall()
                    c=0
                    for i in t:
                        x=i[0]
                        if(x==user):
                            c=1
                            p=0
                            while(p!=1):
                                password=input("Enter password:")
                                cur.execute("select STU_pswd from stuid44")
                                r=cur.fetchall()
                                for j in r:
                                    y=j[0]
                                    
                                    if(y==password):
                                        p=1
                                        cur.execute("select * from stu_details44 where stuser_id = :n", {'n':user})
                                        print("\n***************DETAILS*****************")
                                        z=('Student id: ', 'Name: ', 'Room no: ')
                                        print(z)
                                        print(cur.fetchall())
                                        cur.execute("select days_present from stu_attendance44 where stu_id = :m", {'m':user})
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
                if(n==5):
                    cur.execute("select STUSER_ID from stuid55")
                    t=cur.fetchall()
                    c=0
                    for i in t:
                        x=i[0]
                        if(x==user):
                            c=1
                            p=0
                            while(p!=1):
                                password=input("Enter password:")
                                cur.execute("select STU_pswd from stuid55")
                                r=cur.fetchall()
                                for j in r:
                                    y=j[0]
                                    
                                    if(y==password):
                                        p=1
                                        cur.execute("select * from stu_details55 where stuser_id = :n", {'n':user})
                                        print("\n***************DETAILS*****************")
                                        z=('Student id: ', 'Name: ', 'Room no: ')
                                        print(z)
                                        print(cur.fetchall())
                                        cur.execute("select days_present from stu_attendance55 where stu_id = :m", {'m':user})
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


