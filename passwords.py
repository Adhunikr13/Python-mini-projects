import re
import string
import random

#This function is to test the password strength
def pasword():
    while True:

        Password = input('Enter a strong password:-')

        if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@!#$])[\w\d@!#$]{8,24}$", Password):
            print('Prefect password. Must secure')
            break
        else:
            print('Not a valid password')

def  password_check():

    while (True):
        Pass = input("Enter a valid password")

        if len(Pass)<8:
            print("The password lenght should be more than 8 Characters")

        elif not any(Pass.isupper() for Pass in Pass):
            print("Enter atleat one uppercase letter")

        elif not any(Pass.islower() for Pass in Pass):
            print("Enter atleat one Lowercase letter")

        elif not any(Pass.isdigit() for Pass in Pass):
            print("Enter atleat one Number  between 0 and 1")

        elif Pass.isalnum()== True:
            print("Enter atleast one alphaNumeric")

        else:
            print("password is good :)")
            break
    return Pass

def random_password():

#r"(A-Z)\d(a-z)\d(@!#$)\d(0-9)\d"
# print(rstr(r'[A-Z]\d[0-9]\d', 8))

    password_characters = string.printable
# string.printable : contains all the lowercase, uppercase , special characters
    return ''.join(random.choice(password_characters) for i in range(10))


#To encrypt the password entered by the user

def Caesar_cipher(PasswordInput):
    result = ""
    # transverse the plain text
    for i in range(len(PasswordInput)):
        char = PasswordInput[i]
# Encrypt uppercase characters in plain text

        if (char.isupper() and char.isalpha()):
            #ord() function gives the acii code of the char
            #chr function changes the ascii value to its char
            result += chr((ord(char) + 3 - 65) % 26 + 65)
# Encrypt lowercase characters in plain text
        elif(char.islower() and char.isalpha()):
            result += chr((ord(char) + 3 - 97) % 26 + 97)
#Other chars will remain the same
        else:
            result += char
    return result



option = input("Enter 'a' to Check whether or not a password entered by the user is good\n" "Enter 'b' to Generate a random password instead" )


if option== 'a':

    Input_Password = password_check()
    print(Input_passord)

    WebsiteName = input("Enter the website name")
    UserName = input("Enter the Username for this website")
# Encrypting the User_name and passoword

    EncrptedUserName =    Caesar_cipher(UserName)
    EncrptedPassword = Caesar_cipher(Input_Password)
# Saving the 3 values in tuple
    TupleOf3 = ("Website Name: ", Website_name, "User Name (Encrypted):", Encrpted_userName, "Password (Encrypted):", Encrpted_Pass)
    f = open("passwords.csv", "w+")
    for i in TupleOf3:
        f.write(i)

    f.close()
    print("Your details have been saved in my_passwords.csv file!!")

if option== 'b':
    Random_password = random_password()
    print(Random_password)


    WebsiteName = input("Enter the website name")
    UserName = input("Enter the Username for this website")
    EncrptedUserName = Caesarcipher(UserName)
    EncrptedPassword = Caesarcipher(Random_password)

    TupleOf3 = ("Website Name: ",WebsiteName,"User Name (Encrypted):", EncrptedUserName ,"Password (Encrypted):", EncrptedPasswaord)
    f = open("passwords.csv", "a+")
    for i in TupleOf3:
        f.write(i)


    f.close()
    print("Your details have been saved in passwords.csv file!!")


