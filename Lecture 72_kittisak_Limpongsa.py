menuList = []

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1]) #การผลลัพที่ 0
        #print(menuList[number]) #การเรือกผลลัพทั้งหมด

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuquantity = input("Add your Quantity: ")
        menuList.append([menuName, menuPrice,menuquantity ])

print(menuList)
showBill()
