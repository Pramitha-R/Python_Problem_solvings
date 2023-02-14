import tkinter
from tkinter import *

root=tkinter.Tk()
root.geometry("500x300")


def getvals():
    print("Accept")

#heading of the page
label=tkinter.Label(root,text="python register form",font=('arial',18))
label.grid(row=0,column=3)

#label 
name=tkinter.Label(root,text="name")
name.grid(row=1,column=2)
PhoneNumber=tkinter.Label(root,text="PhoneNumber")
PhoneNumber.grid(row=2,column=2)
gender=tkinter.Label(root,text="genter")
gender.grid(row=3,column=2)
emergency=tkinter.Label(root,text="emergency")
emergency.grid(row=4,column=2)
paymentMood=tkinter.Label(root,text="paymentMood")
paymentMood.grid(row=5,column=2)

#inputes values
nameValue=StringVar()
PhoneNumberValue=StringVar()
genderValue=StringVar()
emergencyValue=StringVar()
paymentMoodValue=StringVar()

checkValue=IntVar()

#inputboxes
nameEntry=Entry(root,textvariable=nameValue)
nameEntry.grid(row=1,column=3)

PhoneNumberEntry=Entry(root,textvariable=PhoneNumberValue)
PhoneNumberEntry.grid(row=2,column=3)

genderEntry=Entry(root,textvariable=genderValue)
genderEntry.grid(row=3,column=3)

emergencyEntry=Entry(root,textvariable=emergencyValue)
emergencyEntry.grid(row=4,column=3)

paymentEntry=Entry(root,textvariable=paymentMoodValue)
paymentEntry.grid(row=5,column=3)

#createsubmit button

submit=tkinter.Button(text="Submit",command=getvals)
submit.grid(row=6,column=3)
root.mainloop()