#open(),read() and readline() of python file:
file = open("kumar.txt",'r')
print(file.readline())#read the first line.
print(file.readline())#read the second line.
content = file.read()#read the all line.
print(content)
file.close()

#Wrintng  to a file:
file = open("kumar1.txt","w")
file.write("Randhir is a good boy\n")
file.close()

#appending to a file:
file = open("kumar1.txt","a")
file.write("Randhir is a good boy\n")
file.close()

# count the character to a file:
file = open("kumar1.txt","a")
a=file.write("Randhir is a good boy\n")
print(a) #a=count the character.
file.close()

# handle read and write to a file
file = open("kumar1.txt","r+")
print(file.read())
file.write("Thank you")
file.close()






