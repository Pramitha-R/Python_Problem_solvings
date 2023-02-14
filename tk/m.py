import tkinter

class Mygui:
    def __init__(self) -> None:
        self.root=tkinter.Tk()
        
        self.label=tkinter.label(self.root,text="your message",font=('Arial',18))
        self.label.pack(padx=10,pady=10)

        self.textbox=tkinter.Text(self.root,font=('Arial',18))
        self.textbox.pack(padx=10,pady=10)

        #self.check=tkinter.Checkbutton(self.root,text="show message",font=)

        self.root.mainloop()

    