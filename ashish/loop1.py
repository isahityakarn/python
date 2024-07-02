num1=int(input("enter first value  : "))
num2=int(input("enter second value : "))
symbol=input("enter the symbol   : ")

if symbol=="+" :
    total=num1+num2
    if total>0:
        print("The total is \t   :",total)
    else:
        print("Disclaimer : The answer is in negative ")
        print("The total is \t   :",total)
elif symbol=="-":
    diff=num1-num2
    if diff>0:
        print("The difference is  :",diff)
    else :
        print("Disclaimer : The answer is in negative ")
        print("The difference is  :",diff)
elif symbol=="*":
    multiply=num1*num2
    if multiply>0:
        print("The product is \t   :",multiply)
    else :
        print("Disclaimer : The answer is in negative ")
        print("The product is \t   :",multiply)
elif symbol=="/":
    division=num1/num2
    if division>0:
        print("The division is    :",division)
    else:
        print("Disclaimer : The answer is in negative ")
        print("The division is    :",division)
else :
    print("Invalid symbol")

