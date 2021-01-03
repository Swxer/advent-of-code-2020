# F, L = lower half
# B, R = upper half

# first 7 char are rows and the remaining 3 are cols

f = open("input.txt", "r")
seat = [line.strip() for line in f]
seats = []

highest_id = 0

for item in seat:
    lo1, hi1 = 0,127
    lo2, hi2 = 0, 7

    # read first 7 char
    for char in item[:7]:
        mid = (lo1 + hi1) // 2
        if char == 'F':
            hi1 = mid
        else:
            lo1 = mid
        row = hi1
        
    # read last 3 char
    for char in item[7:]:
        mid = (lo2 + hi2) // 2
        if char == 'L':
            hi2 = mid
        else:
            lo2 = mid
        col = hi2

    seat_id = row * 8 + col
    seats.append(seat_id)

    if seat_id > highest_id:
        highest_id = seat_id

print(f'{highest_id} is the highest seat id for part 1')

# PART 2

# seats is not at the very front or back
seats.sort()
seats = seats[1:-1]

# if the seats id differ by 2, personal seat id is found

for i in range(1,len(seats)):
    if seats[i] - seats[i - 1] == 2:
        print(f'{seats[i - 1] + 1} is your seat for part 2') 



        
