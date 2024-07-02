i=int(input("enter value to start loop : ")) 
e=int(input("enter value to end loop   : ")) 
if i>=e:
    while i>=e:
        print(i)
        i-=1
else:
    while i<=e:
        print(i)
        i+=1