
list=[1]
for i in range(6):
    print(list)
    list2=[]
    list2.append(list[0])
    for i in range(len(list)-1):
        list2.append(list[i]+list[i+1])
    list2.append(list[-1])
    list=list2
print(list)
  
    
#Initialize a list with the number 1.
#Then, make a new list in each iteration.
#In that list, put in the first element of the old list.
#Then, go through every 2 elements in the list (firstelement+secondele, secondele+thirdele) till you are at the last element, and append every addition to the newlist.
#Finall, append the last element of the oldlist to the new list.
#Print out the list sometime