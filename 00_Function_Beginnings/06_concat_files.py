import datetime

def write_to_file(read, write):
    read_file = open(read, "r")
    content = read_file.read()
    write.write(content + "\n")
    read_file.close()

date = datetime.datetime.now()
file = open(date.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", "w")

write_to_file("file1.txt", file)
write_to_file("file2.txt", file)
write_to_file("file3.txt", file)

file.close()