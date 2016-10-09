grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def print_grid(my_list):
        for i in range(0,len(my_list[0])): # i equals our x coordinate
                my_str = ''
                for j in range(0,len(my_list)): # j equals out y coordinate
                        my_str += my_list[j][i]
                print(my_str)

print_grid(grid)