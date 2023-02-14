num=[12,3,4,5,9]

def find_largest(numbers):
# Your code goes here

    max=0
    if(numbers==[]):
        max="null"
    
    for i in numbers:
        if i>max:
            max=i
 
    return max

print(find_largest(num))