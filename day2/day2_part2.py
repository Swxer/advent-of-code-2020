f = open("input.txt", "r")

valid_count = 0

# loop through the text file
for line in f:

    # separate the line into 3 different components
    component = line.split()

    # separate the range value
    index = component[0].split('-')

    # separate the subject value
    letter = component[1].replace(':','')

    # check if its valid
    if component[2][int(index[0])-1] == letter and component[2][int(index[1])-1] != letter:
        valid_count += 1
    elif component[2][int(index[0])-1] != letter and component[2][int(index[1])-1] == letter:
        valid_count += 1

print(f'{valid_count} valid passwords for part 2')

f.close()