
str="-vnfj0 vdk 78"
 
def getLastNumericalNumber(str):
    m=[]
    num=""
   # print(len(str))
    length=len(str)
    for i in range(0,length):
        if(str[i].isdigit()):
            num+=str[i]
            if(i==length-1):
                m.append(num)
            #print(num)
        elif(num !="" ):
            m.append(num)
            num=""
    if m == []:
        return None
        
    else:
        return m[len(m)-1]


print(getAllNumericalNumber(str))