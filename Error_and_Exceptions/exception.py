# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
new=[]
for i in range(T):
    a,b=input().split()
    
    try:
        value=int(a)/int(b)
        print(int(value))
    except ValueError as v:
        print ("Error Code:",v)
    except ZeroDivisionError as e:
        print ("Error Code: integer division or modulo by zero")
    
