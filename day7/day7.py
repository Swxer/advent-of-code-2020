# copied solution from this youtube video 
# https://youtu.be/7IOd7wvxDX0

f = open("input.txt", "r")

data = [ line.strip() for line in f]

def get_num_bags(colour):

    lines = [ line for line in data if colour in line and line.index(colour) != 0]

    all_colours = []

    # the code above is short for:
    # for line in data:
    #     if colour in line and line.index(colour) != 0:
    #         lines.append(line)

    # if our colour is red and no other bag holds a red bag then it be 0
    if len(lines) == 0:
        return []

    else:
        colours = [ line[:line.index(' bags')] for line in lines ]
        colours = [ colour for colour in colours if colour not in all_colours ]

        for colour in colours:
            all_colours.append(colour)
            bags = get_num_bags(colour)

            all_colours += bags

        unique_colours = []
        for colour in all_colours:
            if colour not in unique_colours:
                unique_colours.append(colour)

        return unique_colours


number = get_num_bags('shiny gold')
print(f'{len(number)} bags for part 1')

# PART 2

def get_bag_count(colour):
    rule = ''
    for line in data:
        if line[:line.index(' bags')] == colour:
            rule = line

    if 'no' in rule:
        return 1

    rule = rule[rule.index('contain')+8:].split()

    total = 0
    i = 0
    while i < len(rule):
        count = int(rule[i])
        colour = rule[i + 1] + ' ' + rule[i + 2]

        total += count * get_bag_count(colour)

        i += 4

    return total + 1

count = get_bag_count('shiny gold') -1
print(f'{count} bags for part 2')

f.close()