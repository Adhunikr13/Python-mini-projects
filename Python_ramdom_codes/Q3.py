import random

def random_no():
    
    
    
    a = [x for x in range (1,1000) if (x%7==0) and (x%5==0)]
    
    a = [random.randint(1,1000) for x in range(5)]
    print(a)
    
c = random_no()
print(c)