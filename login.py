name = input ("Enter your name : ")
password = input ("Enter your password : ")
if name == "yousef" and password == "1234":
    print("Sucsees fully")
elif name == "yousef" or password == "1234":
    print("Nearly")
else:
    print("Sorry try again")