class H:
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        self.name=name
        self.about=about
        self.rooms=rooms
        self.transport=transport
        self.price=price
        self.facilities=facilities
        self.book_now=book_now
        print("-------------------------",self.name,"-------------------------------")
        print("1.About")
        print("2.Rooms")
        print("3.Transport")
        print("4.Facilities")
        print("5.Price")
        print("6.Book now")
        print("7.Student login")
        print("8.Staff login")
        a=10  
        while(a!=0):
            a=int(input("Enter your choice number(options):"))
            print("\n")
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
            if(a==0):
                import p4
                p4.hostel()
            if(a!=0 and a!=1 and a!=2 and a!=3 and a!=4 and a!=5 and a!=6):
                print("------Wrong choice, enter your choice again\n")
    
        
class v_g(H):
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        #Hostel.select(self,name,about,rooms,transport,price,facilities,book_now)
        super().select(name,about,rooms,transport,price,facilities,book_now)
       
class v_b(H):
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        #Hostel.select(self,name,about,rooms,transport,price,facilities,book_now)
        super().select(name,about,rooms,transport,price,facilities,book_now)
class a(H):
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        #Hostel.select(self,name,about,rooms,transport,price,facilities,book_now)
        super().select(name,about,rooms,transport,price,facilities,book_now)
class s(H):
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        #Hostel.select(self,name,about,rooms,transport,price,facilities,book_now)
        super().select(name,about,rooms,transport,price,facilities,book_now)
class p(H):
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        #Hostel.select(self,name,about,rooms,transport,price,facilities,book_now)
        super().select(name,about,rooms,transport,price,facilities,book_now)

obj1= v_g()
obj2=v_b()
obj3=a()
obj4=s()
obj5=p()
