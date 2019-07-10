file = open("example.txt",'r')
content = file.readlines()
content = [i.rstrip("\n") for i in content]
file.close()

print(content)