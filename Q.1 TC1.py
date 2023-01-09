inp1=input("Name:") 
record_name=input("Record name:") 
d1=inp1.split(" ")
d2=record_name.split(" ")
last_d1 = None
last_d2 = None
for token in d1:
    for i, token2 in enumerate(d2):
        if last_d2:
            concat = last_d2 + token2
            if concat == token: 
                d2.remove(last_d2)
                d2.remove(token2)
                d2.insert(i-1, concat)
        if last_d1:
            concat = last_d1 + token
            if concat == token2: 
                d2.remove(token2)
                d2.insert(i, last_d1)
                d2.insert(i+1, token)
        last_d2 = token2
    last_d1 = token
print(" ".join(d2))


