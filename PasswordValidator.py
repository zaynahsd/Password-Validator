import re

userpass = input("Password must be at least 12 characters long. \n Password must contain at least one number. \n Password must contain at least one symbol \n Create a password: ")

def password_validator(userpass):

    if len(userpass) < 12:
        print("Password must be at least 12 characters long.")
        return False

    if not re.search(r'\d', userpass) or not re.search(r'[^\w\s]', userpass):
        print("Password must contain at least one number and one symbol.")
        return False
    
    print("Password is valid.")
    return True

password_validator(userpass)

