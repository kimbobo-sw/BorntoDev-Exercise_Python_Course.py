menuList = []
PriceList = []

def showBill():
    total_price = 0
    print("--------My Food-------------")
    for number in range(len(menuList)):
        print(menuList[number], PriceList[number])
        total_price += int(PriceList[number])
        print(" Total: ",total_price)


while True:
    menuName = input("Please Enter Menu: ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price: ")
        menuList.append(menuName)
        PriceList.append(menuPrice)

print(menuList,PriceList)
showBill()

