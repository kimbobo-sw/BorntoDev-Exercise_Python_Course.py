from tkinter import *
import math
def leftClickButton(event):

    #print(round(float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2))) # คำนวนน้ำหนักส่วนสูง
    #lableResult.configure(text=round(float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2)))#เเสดงคค่าในรูป Gui
    RBMI = (round(float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2)))
    labelBMI.configure(text=RBMI)
    if RBMI < 19.00:
        lableResult.configure(text="อยู่ในเกณฑ์น้ำหนักน้อยผิดปกติ")
    elif RBMI < 24:
        lableResult.configure(text ="น้ำหนักเกณฑ์มาตารฐาน")
    elif RBMI < 25:
        lableResult.configure(text="น้ำหนักเกินเกณฑ์")
    elif RBMI < 30:
        lableResult.configure(text="น้ำหนักอยู่ในเกณฑ์เกิดโลกอ้วน")

MainWindow = Tk()
lableHeight = Label(MainWindow,text="ศ่วนสูง (Cm.)")
lableHeight.grid(row = 0,column =0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)
lableWeight = Label(MainWindow,text="น้ำหนัก (Kg.)")
lableWeight.grid(row = 1,column =0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text ="คำนวน")
calculateButton.grid(row=2,column=0)
calculateButton.bind('<Button-1> ',leftClickButton)
lableResult = Label(MainWindow,text="ผลลัพธ์ ")
lableResult.grid(row = 2,column =1)
labelBMI = Label(MainWindow,text ="เกณฑ์มาตรฐาน")
labelBMI.grid(row=3,column=1)

MainWindow.mainloop()