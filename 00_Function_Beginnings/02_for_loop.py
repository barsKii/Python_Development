import random

myList = [1, 2, 3, 4, 5]
bools = [True, False]

for i in range (20):
    print(str(i) + ") "+ str(random.choice(bools)))