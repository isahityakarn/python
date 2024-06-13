num1=5
num2=1
num3=5

if num1>num2>num3:
    print("big value is :",num1)
elif num2>num1>num3:
    print("big value is :",num2)
elif num3>num2>num1:
    print("big value is :",num3)
elif num2>num3>num1:
    print("big value is :",num2)
elif num1>num3>num2:
    print("big value is :",num1)
elif num3>num1>num2:
    print("big value is :",num3)
elif num1>num2==num3:
    print("big value is :",num1)
elif num2>num1==num3:
    print("big value is :",num2)
elif num3>num1==num2:
    print("big value is :",num3)
elif num1==num2>num3:
    print("big value is :",num1)
elif num2==num3>num1:
    print("big value is :",num2)
elif num3==num1>num2:
    print("big value is :",num3)
else :
    print("all values are same")