# man, lion ,goat, carbage

x=['man','lion','goat','grass']
y=[]
print("x side: ",x)
print("y side: ",y)
while(len(x)!=0):

    print(x[1]," ,",x[2]," , ",x[3]," (select the item)")
    i =input("enter the item : ")

    if (x[1]==i and x[2]=='goat' and x[3]=='grass' ):
        print("goat will eat grass")
        break
    elif x[2]==i and x[3]!='grass':
        y.append(x[2])
        if( len(y)==2 and y[0]=='goat'):
            x[2]=y[0]
            y[0]=y[1]
            y.pop()
    elif x[1]==i and x[2]=='goat':
        y.append(x[1])
        x[1]=x[2]
        x[2]=''
    elif x[1]==i and x[2]=='grass':
        y.append(x[1])
        x[1]=x[2]
        x[2]=''
        if len(y)==2 and y[0]=='goat':
            x[2]=y[0]
            y[0]=y[1]
            y.pop()
    elif x[1]==i and x[2]!='grass' and x[2]!='goat':
        y.append(x[1])
        y.append(x[0])
        x[1]=''
        x=[]
        print("done")
        break
    if(x[2]==1 and x[3]=='grass'):
        y.append(x[2])
        x[2]=x[3]
        x[3]=''
    if(x[3]==i):
        print("lion will ean goat")
        break

print("right side :" ,y)

