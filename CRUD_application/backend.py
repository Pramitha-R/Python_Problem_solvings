import mysql.connector
import tkinter as tk
#from tkinter import *
from tkinter.simpledialog import askstring
from tkinter import ttk,messagebox
from tkinter.messagebox import showinfo
from tkinter import *


mysqldb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
mysqlcursir=mysqldb.cursor(buffered=True)


root=Tk()
root.geometry("800x500")
root.title("car parts")

click=0
global name
global engin
global cost
global id

def Insert_Detail():
    carname=name.get()
    carengin=engin.get()
    carcost=cost.get()
    if (carname=="" and carengin =="" and carcost==""):
        messagebox.showinfo("information","please enter the values! ")
    else:
        sqlquary=f"INSERT INTO `carparts` (`id`, `name`, `engin`, `cost`) VALUES (NULL, '{carname}', '{carengin}', '{carcost}')"
        mysqlcursir.execute(sqlquary)
        mysqldb.commit()
        messagebox.showinfo("information","successfully add the datas.....")
        name.delete(0,END)
        engin.delete(0,END)
        cost.delete(0,END)
        name.focus_set()

        show_detail()

    
def show_detail():
    sqlquary=f"select * from carparts"
    mysqlcursir.execute(sqlquary)
    records=mysqlcursir.fetchall()

    #print(len(records))
    for i in record_table.get_children():
        record_table.delete(i)
    for i in range(len(records)):
        record_table.insert(parent='',index='end',text='',
        iid=i,values=records[i])

def update_detail():
    carname=name.get()
    carengin=engin.get()
    carcost=cost.get()
    carid=id.get()

    sqlquary=f"select * from carparts"
    mysqlcursir.execute(sqlquary)
    records=mysqlcursir.fetchall()
    flag=0
    for i in range(len(records)):
        if int(carid)==records[i][0]:
            flag=1
            if(carname!="" and carengin!="" and carcost!=""):
                sqlquary=f"update carparts set name='{carname}',engin='{carengin}',cost='{int(carcost)}' where id='{carid}'"
                mysqlcursir.execute(sqlquary)
                mysqldb.commit()
                return showinfo("successfully update the data")
                 
            else:
                return showinfo("plz enter the value for corect updation")

    if(flag==0):
        showinfo("invalid index,olz enter the corect index")  
    
def Delete_detail():
    carid=id.get()
    sqlquary=f"select * from carparts"
    mysqlcursir.execute(sqlquary)
    records=mysqlcursir.fetchall()
    flag=0
    for i in range(len(records)):
        if int(carid)==records[i][0]:
            flag=1
            sqlquary=f"delete from carparts where id={carid} "
            mysqlcursir.execute(sqlquary)
            mysqldb.commit()
            showinfo("succesfuly deleted!")
        
    if(flag==0):
        showinfo("invalid index so enter the corect index!")
    

def update_here():

    records=mysqlcursir.fetchall()
    showinfo(records[id][0])
    for i in range(len(records)):
        if(int(id)==records[i][0]):
            name=Entry(root,Text=records[i][1],width=100 )
            name.place(x=140,y=10)

            engin=Entry(root,Text=records[i][2],width=100)
            engin.place(x=140,y=40)
            
            cost=Entry(root,Text=records[i][3],width=100)
            cost.place(x=140,y=40)
            
            #showinfo("car name: {}, car engin name: {} car cost: {}".format(name,engin,cost))


def search_detail():
    fil=search.get()
    sqlquary=f"select * from carparts where name like '{fil}%'"
    mysqlcursir.execute(sqlquary)
    records=mysqlcursir.fetchall()
    
    for i in record_table.get_children():
        record_table.delete(i)
    for i in range(len(records)):
        record_table.insert(parent='',index='end',text='',
        iid=i,values=records[i])

    #id = askstring('edit', 'Index Number?')

#label boxex
Label(root,text="Name" ,font=('Bold',10)).place(x=10,y=10)
Label(root,text="Engin" ,font=('Bold',10)).place(x=10,y=40)
Label(root,text="Cost" ,font=('Bold',10)).place(x=10,y=70)
Label(root,text="ID" ,font=('Bold',10)).place(x=10,y=100)

#inputbox
name=Entry(root,width=100)
name.place(x=140,y=10)

engin=Entry(root,width=100)
engin.place(x=140,y=40)

cost=Entry(root,width=100)
cost.place(x=140,y=70)

id=Entry(root,width=100)
id.place(x=140,y=100)

#buttons
Button(root,text="Show", command=show_detail,height=3,width=13).place(x=30,y=130)
Button(root,text="Delete",command=Delete_detail,height=3,width=13).place(x=140,y=130)
Button(root,text="Insert" ,command=Insert_Detail, height=3,width=13).place(x=250,y=130)
Button(root,text="Update",command=update_detail ,height=3,width=13).place(x=360,y=130)
    

#search bok
Label(root,text='search car name').place(x=30,y=200)
search=Entry(root,width=50)
search.place(x=150,y=200)
Button(root,text="search",command=search_detail,height=1,width=13, ).place(x=500,y=200)

record_frame=tk.Frame(root)
record_table=ttk.Treeview(record_frame)
record_table.pack(fill=tk.X ,pady=5)

#record_table.bind('<Double 1>', car_entry(record_table.selection()))


record_table['column']=['id','name','engin','cost']

record_table.column('#0',anchor=tk.W,width=0,stretch=tk.NO)

record_table.column('id',anchor=tk.W,width=30)
record_table.column('name',anchor=tk.W,width=80)
record_table.column('engin',anchor=tk.W,width=150)
record_table.column('cost',anchor=tk.W,width=100)


#heading table
record_table.heading('id',text='Id',anchor=tk.W)
record_table.heading('name',text='Name',anchor=tk.W)
record_table.heading('engin',text='Engin',anchor=tk.W)
record_table.heading('cost',text='Cost',anchor=tk.W)

record_frame.place(x=10,y=250)
record_frame.pack_propagate(False)
record_frame.configure(width=700,height=800)


root.mainloop()
#show details
mysqldb.close()



