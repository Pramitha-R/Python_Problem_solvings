s = input()

def hashtagGen(text):
	text="#"+text
	s1=text.replace(" ","")
	return s1

print(hashtagGen(s))