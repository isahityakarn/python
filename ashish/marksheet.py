name=input("name \t    : ")
mark1=int(input("hindi marks : "))
mark2=int(input("eng marks   : "))
mark3=int(input("math marks  : "))
print("your hindi mark is :",mark1)
print("your eng mark is   :",mark2)
print("your math mark is  :",mark3)
total=mark1+mark2+mark3
print("your total is \t   :",total)
avg=total/3
print("your average is\t   :",avg)
if avg>60 :
    print("1st")
elif avg>45:
    print("2nd")
else :
    print("3rd")
if mark1>=33 and mark2>=33 and mark3>=33:
    print("pass")
else :
    print("fail")
