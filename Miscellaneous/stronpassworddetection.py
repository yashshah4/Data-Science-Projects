import re

def pswd():
    while True:
        text = str(input("Please enter a password : "))

        if len(text)>=8:
            upRegex = re.compile(r'[A-Z]')
            loRegex = re.compile(r'[a-z]')
            diRegex = re.compile(r'[0-9]')
            mo = upRegex.search(text).groups()
            mo1 = loRegex.search(text).groups()
            mo2 = diRegex.search(text).groups()
            if mo == None or mo1 == None or mo2 == None:
                print("Password must contain atleast 1 uppercase, 1 lowercase & 1 digit")
                continue
            else:
                print("This is a strong password!")
                break
        else:
            print("Password needs to be atleast 8 characters long")
            continue

pswd()   
