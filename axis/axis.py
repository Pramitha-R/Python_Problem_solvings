import random

rands=[]
for i in range(0,33):
    x=random.random()
    y=random.random()
    rands.append([x,y])


def pi_approx(pts):
    SatisfyTheCircle=[]
    for i in range(0,len(pts)):
        point=pts[i]
        x=point[0]
        y=point[1]
        
        result=x**2 + y**2
        if(result<=1):
            if(x==1 and y==0):
                print("point(1,0) is inside")
            SatisfyTheCircle.append(point)
        
    #print("point(1,0) is here: ", val==1)
    aproximateValue=4*(len(SatisfyTheCircle)/len(pts))
    return aproximateValue
    #return SatisfyTheCircle

print(pi_approx(rands))
    


    
    

