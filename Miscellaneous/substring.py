''' Given two strings, string1 and string2, the function below finds out
if string1 is a subsequence of string2. A subsequence is a sequence that
can be derived from another sequence by deleting some elements without
changing the order of the remaining elements.
Example:

string1 = 'abc'
string2 = 'asbsc'
string3 = 'acedb'

isSubSequence(string1, string2) -> True
isSubSequence(string1, string3) -> False
'''
# defining the function
def substring(s1,s2):
    s11 = list(s1)  # converting strings into lists
    s21 = list(s2)  # converting strings into lists
    n = []
    for i,e in enumerate(s11):  # looping through s11
        if e in s21:    #checking if the character is in s21
            q = s21.index(e) # saving the index of character in q
            n.append(q) # appending the index in a new list
            s21[q] = '0'    # replacing the character with 0 to tackle duplicates

    if sorted(n) == n: # checking if the sequence of characters is the same in s21
        print(s1 + ' is a subsequence of '+ s2)
    else:
        print(s1 + ' is NOT a subsequence of ' + s2)
# Taking the input values from teh user
s1 = str(input("Please enter the first string : "))
s2 = str(input("Please enter the second string : "))
substring(s1,s2)
