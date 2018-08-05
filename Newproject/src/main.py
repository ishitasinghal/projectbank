import sys
def hostel():
    from hostelpackage import hosteldetail
    n=6
    while(n!=0):
        print("-------------HOSTELS IN DEHRADUN-------------\n")
        print("1. Vatika Girls Hostel")
        print("2. Vatika Boys Hostel")
        print("3. Aman Residency (Boys)")
        print("4. Sarthak Boys Hostel")
        print("5. Pride Girls Hostel")
        print("[Press 0 to exit]")
        n=int(input("Enter your choice number(hostel):"))
        if(n==1):
            hosteldetail.vatika_girls()
        if(n==2):
            hosteldetail.vatika_boys()
        if(n==3):
            hosteldetail.aman_residency()
        if(n==4):
            hosteldetail.sarthak()
        if(n==5):
            hosteldetail.pride()
        if(n!=0 and n!=1 and n!=2 and n!=3 and n!=4 and n!=5):
            print(">>>>Wrong choice, enter your choice again\n")
    if(n==0):
        sys.exit()
            
