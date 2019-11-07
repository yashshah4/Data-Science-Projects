message = str(raw_input("Enter a text : "))
count={}
for chara in message:
    count.setdefault(chara,0)
    count[chara]= count[chara]+1
print (str(count))
