import sys
import math
from contextlib import redirect_stdout


def solve(width, height, length, mass): # Write your code here
    volume=width*height*length
    bulky ,heavy=False,False
    if (volume>=1000000 or width>=150 or height>=150 or length >=150):
        bulky=True
    if mass>=20:
        heavy=True
        

    if(bulky==False or heavy==False):
        x= "STANDARD"
    elif((bulky ==False and heavy==True) or (bulky ==True and heavy==False) ):
        x= "SPECIAL"
    else:
        x= "REJECT"
    return x
 # To debug: print("Debug messages...", file=sys.stderr, flush=True)
 



 # Ignore and do not change the code below
def main():
    while True:
        width, height, length, mass = [int(i) for i in input().split()]
        with redirect_stdout(sys.stderr):
            if(width<=200 and height<=200 and length<=200 and width >=20):
                action=solve(width, height, length, mass)
            print(action)
       


if __name__ == "__main__":
    main()
 # Ignore and do not change