#The following module helps prettify the printout of a dictionary
#This module includes pprint() & pformat() to improve what print() generally offers
import pprint
#Asking for a text input from the user and saving it as a string
message = str(raw_input("Enter a text : "))
#Declaring a dictionary to count characters
count={}
#iterating through each character
for chara in message:
    count.setdefault(chara,0)
    count[chara]= count[chara]+1
pprint.pprint (str(count))
#If you want to obtain the prettified text as a string value instead of
#dis- playing it on the screen, call pprint.pformat() instead
# pprint.pformat(count)
