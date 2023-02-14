import tkinter 

root=tkinter.Tk()
root.title("my first title")

label=tkinter.Label(root, text="Hello world! ",font=('Arial',18))
label.pack(padx=10,pady=10)

textbox=tkinter.Text(root,height=3,font=('Arial',20))
textbox.pack(padx=10,pady=10)

button=tkinter.Button(root,text="click here",font=('Arial',20))
button.pack(padx=10,pady=10)

buttonframe=tkinter.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

btn1=tkinter.Button(buttonframe,text="1",font=('arial',18))
btn1.grid(row=0,column=0,sticky=tkinter.W+tkinter.E)

btn2=tkinter.Button(buttonframe,text="2",font=('arial',18))
btn2.grid(row=0,column=1,sticky=tkinter.W+tkinter.E)

btn3=tkinter.Button(buttonframe,text="3",font=('arial',18))
btn3.grid(row=0,column=2,sticky=tkinter.W+tkinter.E)

btn4=tkinter.Button(buttonframe,text="4",font=('arial',18))
btn4.grid(row=1,column=0,sticky=tkinter.W+tkinter.E)

btn5=tkinter.Button(buttonframe,text="5",font=('arial',18))
btn5.grid(row=1,column=1,sticky=tkinter.W+tkinter.E)

btn6=tkinter.Button(buttonframe,text="6",font=('arial',18))
btn6.grid(row=1,column=2,sticky=tkinter.W+tkinter.E)

buttonframe.pack(fill='x')



root.mainloop()