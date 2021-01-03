f = open("input.txt", "r")

form = [line.strip() for line in f]
letters = []

total = 0
current_string = ''
for item in form:

    # combine a group into a single string
    if item != '':
        # add distinct letter in a group to a list
        current_string += item
        for char in current_string:
            if char not in letters: letters.append(char)
    else:
        # count distinct letter in the group and add to the total
        total += len(letters)
        current_string = ''
        letters = []

# the very last group since it doesnt end with ''
total += len(letters)

print(f'{total} questions people answered "yes" for part 1')

# PART 2 

def get_unique_ans(current_string):
    # check common letters from list of strings
    common_q = []

    for char in current_string[0]:
        in_all_lines = True
        for line in current_string:
            if char not in line:
                in_all_lines = False

        if in_all_lines and char not in common_q:
            common_q.append(char)

    return len(common_q)

total = 0
current_string = []

for item in form:
    if item != '':
        current_string.append(item)
    else:
        total += get_unique_ans(current_string)
        current_string = []

# very last group
total += get_unique_ans(current_string)

print(f'{total} questions everyone answered "yes" for part 2')

f.close()