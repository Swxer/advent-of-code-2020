
f = open("input.txt", "r")

valid_count = 0

# loop through the text file
for line in f:

    # separate the line into 3 different components
    component = line.split()

    # separate the range value
    size = component[0].split('-')

    # separate the subject value
    letter = component[1].replace(':','')

    # count how many letter 
    letter_count = component[2].count(letter)

    # check if its valid
    if letter_count >= int(size[0]) and letter_count <= int(size[1]):
        valid_count += 1

print(f'{valid_count} valid passwords for part 1')

f.close()
