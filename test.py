from datetime import date

a=6
b=8
list1 =[1,2,3,6,8]

def ifstatement():
    if a<5:
        print(a+b)
    else:
        print(0)

# SIMPLE IF STATEMENT
def listcheck():
    if a in list1:
        if b in list1:
            print("A & B are found in the list")
        else:
            print("Only A in the list")
    elif b not in list1:
        print("A & B are not found in the list")
    else:
        print("Only B  found in the list")

# USER INPUT
def inputs():
    name = input("What's your name? ")
    age = int(input("What's your age? "))

    currentdate = date.today()
    currentyear = currentdate.year
    print(currentdate)
    print(currentyear)
    yob= currentyear - age  


    print(f"Welcome {name}. Your DOB is {yob}")
                   

def list1_loop():
    for i in list1:
        print(i)




# ifstatement()
# listcheck()
# inputs()
list1_loop()


