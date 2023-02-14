"""with open ('myfile.txt') as file:
    print(file.read())
print(file.close)"""
txt="i am pemmi"
with open('myfile.txt','w') as file:
    print(file.write(txt))

print(file.closed)