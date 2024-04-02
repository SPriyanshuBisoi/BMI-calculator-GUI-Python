import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


root = tk.Tk()

root.geometry("540x620+0+0")
root.resizable(0,0)
root.title("BMI")
root.configure(bg="#ffffff") 

def BMI_cal():
    BHeight = float(var2.get())
    Bweight = float(var1.get())
    BMI = str('%.2f' %(Bweight / (BHeight * BHeight)))
    lblBMIResult. config(text=BMI)
       
var1 = DoubleVar()
var2 = DoubleVar()


Tops=Frame(root, width=700, height=50, bd=8, relief="raise")
Tops.pack(side=TOP)
f1 = Frame(root, width = 600,height = 600, bd=8, relief="raise")
f1.pack(side=TOP)
f2 = Frame(root, width = 300,height = 700, bd=8, relief="raise")
f2.pack(side=BOTTOM)



fla = Frame(f1, width = 600,height = 20, bd=10, relief="raise")
fla.pack(side=TOP)
flb = Frame(f1, width = 600,height = 600, bd=10, relief="raise")
flb.pack(side=TOP)




lblTitle=Label(Tops, text= "      BODY MASS INDEX  " ,padx=5,pady=5, bd=5,
               fg="#ffffff", font=('times new roman',25,'bold'),
               bg="#d8135b",relief = 'raise',width = 25, height = 1)
lblTitle.pack()

lblweight=Label (fla, text = "SELECT  WEIGHT  IN  KILOGRAMS ",font=('times new roman', 15, 'bold'), bd=20).grid(row = 0,column=0)
Bodyweight = Scale(fla, variable = var1, from_= 1, to=150, length=494,tickinterval=10,orient=HORIZONTAL)
Bodyweight.grid(row = 1,column=0)


lblheight=Label(flb, text = "ENTER  HEIGHT  IN  METERS ",font=('times new roman',15,'bold'), bd=20).grid(row = 0,column=0)
txtheight = Entry(flb, textvariable = var2, font=('times new roman',16,'bold' ),bd=16, width=12,justify='center')
txtheight.grid(row = 1, column=0)




lblBMIResult = Label(flb, padx=5,pady=5, bd=5,
                     fg="#fffaff", font=('arial',30,'bold'),
                     bg="#3e92cc", relief = 'sunk',width = 20, height = 1)
lblBMIResult.grid(row = 2, column=0)

image = Image.open("bmi.jpg")
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.pack()


btnBMI = Button(f2, text="BMI",padx=5,pady=5,bd=5, width =15,
                font=('times new roman',11,'bold'), height=1, command =BMI_cal)
btnBMI. grid(row = 2,column=0)

root.mainloop()

