f = open("input.txt", "r")

data = [ line.strip() for line in f ]

def get_acc_before_loop():
    visited_line = []

    accumulator = 0
    i = 0
    while i not in visited_line:
        visited_line.append(i)

        num = data[i].split()[1]
        if 'acc' in data[i]:
            accumulator += int(num)
            i += 1
        elif 'jmp' in data[i]:
            i += int(num)
        elif 'nop' in data[i]:
            i += 1
    
    return accumulator

acc = get_acc_before_loop()
print(f'accumulator before infinite loop is {acc} for part 1')

# PART 2
def get_acc_without_loop():
    visited_line = []

    accumulator = 0
    i = 0
    while i not in visited_line:
        visited_line.append(i)

        num = data[i].split()[1]
        if 'acc' in data[i]:
            accumulator += int(num)
            i += 1
        elif 'jmp' in data[i]:
            i += int(num)
        elif 'nop' in data[i]:
            i += 1

        if i >= len(data):
            return accumulator, True
    
    return accumulator, False

for i in range(len(data)):
    if 'jmp' in data[i]:
        data[i] = data[i].replace('jmp', 'nop')

        acc, found = get_acc_without_loop()

        if found:
            print(f'accumulator without the loop is {acc} for part 2')
            break
        else:
            data[i] = data[i].replace('nop', 'jmp')


f.close()