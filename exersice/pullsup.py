file = open("/usercode/files/pull_ups.txt")
n = int(input())

results=file.readlines()
print(results[n])
#your code goes here


file.close()