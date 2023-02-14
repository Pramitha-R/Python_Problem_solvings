l1=[]


def closedToZero(num):
    #print(num)
    if(len(num)==None):
        return 0
    
    how=0.0
    for i in num:
        if(how==0.0):
            how=i
        elif(i >0 and i<=abs(how)):
            how=i
        elif(i<0 and abs(i)<abs(how)) :
            how=i
        
    return how

print(closedToZero(l1))