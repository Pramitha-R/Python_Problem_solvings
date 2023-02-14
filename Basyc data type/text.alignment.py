width=int(input())
sum=0
for i in range(width+1):
    print(('H'*(2*i-1)).rjust((width+i),' '))
    sum=width+i

for i in range(width+1):
    print((('H'*width).center((sum+1),' ')),end="")
    print((('H'*width).center(2*(sum+1),' ')))

for i in range(3):
    print(('H'*width*5).center(3*(sum)-3,' '))

for i in range(width+1):
    print((('H'*width).center((sum+1),' ')),end="")
    print((('H'*width).center(2*(sum+1),' ')))

for i in range(width+1,1,-1):
    print(('H'*(2*i-1)).rjust(2(sum+1),' '))
    sum=width+i