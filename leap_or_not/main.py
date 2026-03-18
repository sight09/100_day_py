# leap or not

leap = int(input("enter the year u wanna to check"))

if leap % 4 == 0:
    if leap % 100 == 0:
        if  leap % 400 == 0:
            print("leap")
        else:
            print("not")    
    else:
        print("leap")
else:
    print("not ") 


