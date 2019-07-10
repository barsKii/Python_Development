def convert_temp(C):
    if C < -273.15:
        return "You have selected a temperature that doesn't exist."
    else:
        with open("ctof.txt", "a+") as file:
            file.write(str((C*9)/5 + 32) + "\n")
        return (C*9)/5 + 32

temperatures=[10,-20,-289,100]

for temps in temperatures:
    print(convert_temp(temps))