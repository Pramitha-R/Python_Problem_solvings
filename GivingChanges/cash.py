ten=0
five=0
two=0
def change(cash):
# Your code goes here
    
    global ten,five,two
    if(cash >0 and cash %2==0):
       
        while(cash>=10):
            ten+=1
            cash-=10
        while(cash>=2):
            two+=1
            cash-=2
    elif( cash>=5 and cash %2==1):
        
        while(cash>=15):
            ten+=1
            cash-=10
            
        if(cash<15):
            five+=1
            cash-=5
            return change(cash)
    if(cash<=3 and cash!=0):
        return( "Imposible")
    else:
        return{
            'two':two,
            'five':five,
            'ten':ten
        }

print(change(13))
