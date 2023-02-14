
str="avc98"
 
def getAllNumericalNumber(str):
    m=[]
    num=""
   # print(len(str))
    t=len(str)
    for i in range(0,t):
        if(str[i].isdigit()):
            print(str[i])
            num+=str[i]
            if(i==t-1):
                m.append(num)
            #print(num)
        elif(num !="" ):
            m.append(num)
            num=""
    return m


print(getAllNumericalNumber(str))