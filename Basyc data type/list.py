if __name__ == '__main__':
    N = int(input())

value=[]
for i in range(N):
    key=input().split()
    
    if(key[0]=="print"):
        print(value)
    elif(key[0]=="remove"):
        value.remove(int(key[1]))
    elif(key[0]=="insert"):
        value.insert(int(key[1]),int(key[2]))
    elif(key[0]=="append"):
        value.append(int(key[1]))
    elif(key[0]=="sort"):
        value.sort()
    elif(key[0]=="pop"):
        value.pop()
    elif(key[0]=="reverse"):
        value.reverse()
    else:
        print("somthing went wrong ",value)

    
