file = open("names.txt", "w")
#write down the names into the file
for word in names:
    file.write(word+'\n')
file.close()
file= open("names.txt", "r")
print(file.read())
#output the content of file in console


file.close()