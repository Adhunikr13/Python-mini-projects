
def fname():
    lst = [] 
    input_string = input("Enter Student FirstName separated by comma ")
    fname_list  = input_string.split(",")
    print("Printing all students First names")
    for fname in fname_list:
        print(fname)
    c =  sorted(fname_list, key=str.lower)
    
    print("Alpha sorted First Name")
    print(c)
    
def lname():
    lst = [] 
    input_string = input("Enter Student LastName separated by comma ")
    lname_list  = input_string.split(",")
    print("Printing all students Last names")
    for lname in lname_list:
        print(lname)
    c = sorted(lname_list, key=str.lower)
    
    print("Alfha sorted LastName")
    print(c)
    
def BirthMon():
    lst = [] 
    input_string = input("Enter Student Birth Month separated by comma(no zero forex:- '01') ")
    birmon_list  = input_string.split(",")
    print("Printing all students BirthMonth")
    for birmon in birmon_list:
        print(birmon)
    birmon_list.sort()
    print(birmon_list)

def BirthYr():
    lst = [] 
    input_string = input("Enter Student Birth Year separated by comma")
    biryr_list  = input_string.split(",")
    print("Printing all students BirthYear")
    for biryr in biryr_list:
        print(biryr)
    biryr_list.sort()
    print(biryr_list)
    
    

fname()
lname()
BirthMon()
BirthYr()