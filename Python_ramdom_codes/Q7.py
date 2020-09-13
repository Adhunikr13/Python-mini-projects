
#I used a inbuilt function beacuse was not able to do it on list, I tried but was only able to do it with file
from collections import Counter
text =  input("Enter Animal names ")
 
c = dict(Counter(text.replace(',', '').replace('.', '').split()))
print("Dict from List")
print(c)


#2nd part used a for loop to ittrate through all the elements

inverted = dict()
for key, value in c.items():
    inverted.setdefault(value, list()).append(key)
print("Inverted Dict")
print(inverted)


print("Sorted invert dict by key")
for i in sorted (inverted) : 
    print ((i, inverted[i]), end =" ")