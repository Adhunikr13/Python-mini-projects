def is_leapyear():

    year = int(input("Please Enter the Year Number you wish: "))

    if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
        return True
    else:
        return False
    
c = is_leapyear()
print(c)