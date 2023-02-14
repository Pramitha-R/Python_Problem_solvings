
def largenumber(li):
    """max=0
    for i in li:
        if i>=max:
            max=i"""
    m=max(li)
    return m

li=[6,3,4,5,9]
if (len(li)==1):
    print(li[0])
else:
    print(largenumber(li))