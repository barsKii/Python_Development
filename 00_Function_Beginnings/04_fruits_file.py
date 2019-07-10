file = open("fruits.txt", 'r')
content = file.readlines()

file.close()

for i in content:
    print(len(i.strip()))

#print(content)