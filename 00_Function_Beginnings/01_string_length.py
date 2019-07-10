def length(string):
    if type(string) == int:
        return "Integers aren't accepted"
    elif type(string) == float:
        return "Floats aren't accepted"
    else:
        return len(string)

print(length(float(11.3)))