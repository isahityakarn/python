name=input("enter your name\t        : ")
basic_salary=int(input("enter your basic salary : "))
TA=basic_salary*5/100
print("TA  :",TA)
DA=basic_salary*6/100
print("DA  :",DA)
HRA=basic_salary*7/100
print("HRA :",HRA)
PF=basic_salary*8/100
print("PF  :",PF)
ESI=basic_salary*9/100
print("ESI :",ESI)
Gross_salary=basic_salary+TA+DA+HRA
print("Your gross salary is :",Gross_salary)
Net_salary=Gross_salary-PF-ESI
print("Your net salary is   :",Net_salary)
Annual_salary=Net_salary*12
IT=(Annual_salary-300000)*10/100
if Annual_salary>300000:
    print("IT : ",IT)
else :
    print("NO IT")