from tkinter import *

def leftClickButton(event):
    try:
        cal = eval(textinput1.get())
        labelResultVar.set(cal)
    except Exception as e:
        labelResultVar.set("Error: " + str(e))

main = Tk()

Inputvalue1 = Label(main, text="Input your Values")
Inputvalue1.grid(row=0, column=0)

textinput1 = Entry(main)
textinput1.grid(row=0, column=1)

calculateButton = Button(main, text="Calculate")
calculateButton.grid(row=1, column=1)
calculateButton.bind('<Button-1>', leftClickButton)

labelResultVar = StringVar()
labelResult = Label(main, textvariable=labelResultVar)
labelResult.grid(row=2, column=1)

main.mainloop()