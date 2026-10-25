num1=float(input("Enter Frist Number : "))
oper=input('Choose An Opperation (+,-,*,/,% ):')
num2=float(input("Enter Secound Number : "))
if oper =="+":
    result = num1+num2
    print(num1,"+",num2, "=",result)
elif oper =="-":
    result = num1-num2
    print(num1,"-",num2, "=",result)
elif oper =="*":
    result = num1*num2
    print(num1,"*",num2, "=",result)
elif oper =="/":
    result = num1/num2
    print(num1,"/",num2, "=",result)
elif oper =="%":
    result = num1%num2
    print(num1,"%",num2, "=",result)
else: print("Error")
