def find_trees(right, down):
    '''
    part 1 is taken cared of for right 3 and down 1
    part 2 you can manually multiply the results
    '''
    f = open("input.txt", "r")

    # the tobaggan path loops every 31 index traversal

    index_pos = 0
    tree_count = 0
    down_temp = down

    # ensure it doesnt go down on the starting point
    start = 0

    # the slope/gradient is 3 right and 1 down
    # . -> open path, # -> tree
    
    for row in f:

        if down_temp != 1 and start_flag != 0:
        # should there be a different value for 'down'
            down_temp -= 1
            # continue to the next iteration straight away
            continue
        down_temp = down

        # account for looping if it went past the max row index
        index_pos = index_pos % 31

        # at start of every iteration, check if tree is landed
        if row[index_pos] == '#':
            tree_count += 1

        # go to the right by 3
        index_pos += right

        # starting position has been checked
        start = 1

    print(f'{tree_count} trees with slope right {right}, down {down}')

    f.close()

find_trees(1,1)
find_trees(3,1)
find_trees(5,1)
find_trees(7,1)
find_trees(1,2)










