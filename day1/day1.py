# open file
f = open("input.txt", "r")

# convert those numbers into list
l = [int(x) for x in f]

# find the two pairs that adds up to 2020
for x in l:
    for y in l:
        if x + y == 2020:
            # if the pair is found, multiply and show result
            print(x*y)

# for part 2
for x in l:
    for y in l:
        for z in l:
            if x + y + z == 2020:
                print(x*y*z)
