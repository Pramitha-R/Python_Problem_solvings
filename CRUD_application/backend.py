import mysql.connector
mysqldb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
mysqlcursir=mysqldb.cursor(buffered=True)

#mysqlcursir.execute("create table carParts(id INT auto_increment primary key, name varchar(30),engin varchar(30),cost int)")

def show_detail():
    mysqlcursir.execute("select * from carParts")
    records=mysqlcursir.fetchall()
    print(records)
    

def Insert_Detail():
    name, engin,cost=input("enter the car name, engin, cost : ").split() 
    sqlquary=f"INSERT INTO `carparts` (`id`, `name`, `engin`, `cost`) VALUES (NULL, '{name}', '{engin}', '{int(cost)}')"
    mysqlcursir.execute(sqlquary)
    mysqldb.commit()
    show_detail()

def delete_data():
    n=int(input("Enter the index : "))
    sqlquary=f"delete from carparts where id={n} "
    mysqlcursir.execute(sqlquary)
    mysqldb.commit()
    show_detail()

def update_data():
    n=int(input("Enter the update the index : "))
    mysqlcursir.execute(f"select * from carparts where id={n}")
    print(mysqlcursir.fetchall())
    name,engin,cost=input("enter the upate name, engin ,cost: ").split()
    sqlquary=f"update carparts set name='{name}',engin='{engin}',cost='{int(cost)}' where id={n} "
    mysqlcursir.execute(sqlquary)
    mysqldb.commit()
    show_detail()

def filterBySomthing():
    fil=input("enter the world or letter: ")
    sqlquary=f"select * from carparts where name like '{fil}%'"
    mysqlcursir.execute(sqlquary)
    records=mysqlcursir.fetchall()
    print(records)
    #mysqldb.commit()
    
    
    
    
    
    #    print("not found")

print("1.Show carParts")
print("2.Delete")
print("3.Insert")
print("4.Update")
print("5.exit")
print("6.filtersomthing")


print("---------------------")
i=1
while(i==1):
    op=int(input("Enter the option number: "))
    if(op==1):
        show_detail()
        
    elif(op==2):
        delete_data()
        
    elif(op==3):
        Insert_Detail()
        
    elif(op==4):
        update_data()
    elif (op==6):
        filterBySomthing()
        
    elif(op==5):
       i=2
    else:
        pass


mysqldb.close()



