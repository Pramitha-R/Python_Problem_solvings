li=[80, 1, 4, 25, 12, 60, 78, 70]

temp=sorted(li)

print(temp)
def getminNumber(temp):
    min=1000
    for i in range(len(temp)-1):
     
        if(temp[i+1]-temp[i] <= min ):
            min=temp[i+1]-temp[i]
    return min
    
print(getminNumber(temp))