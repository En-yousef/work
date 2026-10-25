drink = input("Enter Your Drink (coffe / tea) : ")
if drink == "coffe":
    coffe_type = input("Do you need it black or suger : ")
    if coffe_type == "black":
        print("nice black coffe for you")
    elif coffe_type == "suger":
            print("nice suger coffe for you")
elif drink == "tea":
    tea_type = input("Do you need it red or green : ")
    if tea_type == "red":
        print("nice red tea for you")
    elif tea_type == "green" :
        print("nice green tea for you")
else:
    print("sorry ")
