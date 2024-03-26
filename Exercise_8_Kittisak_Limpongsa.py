

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