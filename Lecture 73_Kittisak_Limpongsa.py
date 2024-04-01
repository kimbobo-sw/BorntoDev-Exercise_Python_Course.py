Pricelist = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}
menuList = []

def showBill():
    total_price = 0
    print("---- My Food----")
    for number in range(len(menuList)):

        print(menuList[number][0],menuList[number][1]) #การผลลัพที่ 0
        total_price += menuList[number][1]
        print("Total Price: ", total_price)
        #print(menuList[number]) #การเรือกผลลัพทั้งหมด

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:

        menuList.append([menuName, Pricelist[menuName]])

showBill()