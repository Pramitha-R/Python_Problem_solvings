import sys
import math
from contextlib import redirect_stdout


def calculate_total_price(prices, discount):

    try:
        x=max(prices)
        if x>=100000:
            print("this price has large discount ")
        prices.remove(x)
        value=x-x*(discount/100)
        prices.append(value)
        print(prices)
        sum=0
        for i in prices:
            sum+=i
        return int(sum)
    except(ValueError):
        prices==None
        return print("no sale")


def main():
    # pylint: disable = C, W
    discount = int(input())
    #n = int(input())
    prices = [int(i) for i in input().split()]
    with redirect_stdout(sys.stderr):
        price = calculate_total_price(prices, discount)
    print(price)

if __name__ == "__main__":
    main()
 # Ignore and do not change the code above
