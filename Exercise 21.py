from tkinter import *
import math

def leftClickButton(event):

    BMI = (round(float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2)))
    labelBMI.configure(text=BMI)
    if BMI <= 18.5:
        lableResult.configure(text="อยู่ในเกณฑ์น้ำหนักน้อยผิดปกติ" )
    elif BMI <= 22.9:
        lableResult.configure(text="น้ำหนักปกติ เหมาะสม" )
    elif BMI <= 24.9:
        lableResult.configure(text="น้ำหนักเกิน" )
    elif BMI <= 29.9:
        lableResult.configure(text="อ้วน" )
    elif BMI <= 30.0:
        lableResult.configure(text="อ้วนมาก" )






MainWindow = Tk()

lableHeight = Label(MainWindow, text = "ส่วนสูง (Cm.)")
lableHeight.grid(row = 0,column = 0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)
lableWeight = Label(MainWindow,text ="น้ำหนัก (Kg.)")
lableWeight.grid(row =1,column =0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row = 1, column =1)
calculateButton = Button(MainWindow,text="คำนวน")
calculateButton.grid(row=2,column =0)
calculateButton.bind('<Button-1> ',leftClickButton)
lableResult = Label(MainWindow, text = "ผลลัพธ์")
lableResult.grid(row = 2,column =1)
labelBMI = Label(MainWindow, text = "เกณฑ์มาตรฐาน")
labelBMI.grid(row=3,column=1)

MainWindow.mainloop()


