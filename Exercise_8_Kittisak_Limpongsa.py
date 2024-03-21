
'''''''''
Username = input("Input your ID: ")
Password = input("Input your Password: ")

if Username == "kim": # กำหนดรหัสที่ถูกต้อง
    print("ok !")
if Password == "1234": # กำหนด Password ที่ถูกต้อง
    print("Pls go to your side")
    print("Input Your Money")
    print("In put your Income")
    print("In put Your cost")
    user_selected = int(input(">>: "))

    if  user_selected == 1: # กำหนดเงือนไขเเรก
        money = int(input("Your Money: "))
        incomePerfay = int(input("Your Income: "))
        costPerDay = int(input("CostPerDay: "))
        Result = ((incomePerfay + money) * 30) - (money * 30)
        print(Result)
    elif user_selected == 2: # กำหนดเงือนไขที่ 2
        Product1 = int(input("First Product Price : "))
        Product2 = int(input("Second Product Price : "))
        Total_price = Product1+Product2
        print("Total Price = ",Total_price)
'''''''''''

Username = input(" Input You ID: ")
Password = input(" Input Your Password: ")

if Username == "kim" and Password == "1234":
    print("======================================")
    print(" Welcome ")
    print(" What you want to buy ? ")
    print("Please select your product ")
    print("=======================================")
    print(" 1.Apple 30 BATH Per Piece" )
    print(" 2.Tomato 50 BATH Per Piece" )

    selected = int(input(">>> "))

    if selected == 1:
        print(" Apple 30 BATH Per Piece")
        
        Number_Product = int(input("How Many do you want:  "))
        x = Number_Product * 30
        print("Total Price = ",x, "BATH")

    elif selected == 2:    
        print(" Tomato 50 BATH Per Piece")

        Number_Product = int(input("How Many do you want:  "))
        x = Number_Product * 50
        print("Total Price = ",x, "BATH")
    else:
        print("Please insert your number")
else:
    print("Please Insert Your Correct ID and Password")        