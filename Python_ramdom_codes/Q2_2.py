def is_vowel():
    
    ch = input("Enter a character: ")

    if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
    or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        return True
    else:
        return False
    
f = is_vowel()
print(f)