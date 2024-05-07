def find_start_location(location_map):
    for row_idx, row in enumerate(location_map):
        for col_idx, cell in enumerate(row):
            if cell == 'S':
                return col_idx, row_idx
    return None

def is_valid_location(location_map, col, row):
    num_rows = len(location_map)
    num_cols = len(location_map[0]) 
    return 0 <= row <= num_rows and 0 <= col <= num_cols

def generate_pipe_locations(location_map, pipe_map, start_col, start_row):
    direction_attempts = [[1,0], [0,1], [-1,0], [0,-1]]
    current_row, current_col = start_row, start_col
    
    for direction_attempt in direction_attempts:
        current_direction = direction_attempt
        current_row = start_row + current_direction[1]
        current_col = start_col + current_direction[0]
        pipe_locations = [[start_col, start_row]]
        loop = True
        while loop:
            pipe_checks = 0
            for pipe, directions in pipe_map:
                str = location_map[current_row][current_col]
                if str != pipe:
                    pipe_checks += 1
                    if pipe_checks == 6:
                        loop = False
                        break
                    continue
                pipe_locations.append([current_col, current_row])
                for direction in directions:
                    if direction == [current_direction[0] * (-1), current_direction[1] * (-1)]:
                        continue
                    current_direction = direction
                    next_col = current_col + current_direction[0]
                    next_row = current_row + current_direction[1]
                    if not is_valid_location(location_map, next_col, next_row):
                        loop = False
                        break
                    if location_map[next_row][next_col] == 'S':
                        return pipe_locations
                    current_row, current_col = next_row, next_col
                    break
        raise Exception("Pipe not found")

def generate_location_map(file):
    with open(file, 'r') as file:
        location_map = list(list(line.strip()) for line in file)
    return location_map

def count_enclosed_tiles(location_map, pipe_locations):
    enclosed_tiles = 0
    for row_idx, row in enumerate(location_map):
        for col_idx, _ in enumerate(row):
            current_row = row_idx
            current_col = col_idx
            location = [current_col, current_row]
            if location in pipe_locations:
                continue
            jordan_counter = 0
            in_map = True
            while in_map:
                current_row += 1
                if current_row >= len(location_map):
                    in_map = False
                elif location_map[current_row][current_col] == '-' and [current_col, current_row] in pipe_locations:
                    jordan_counter += 1
                elif location_map[current_row][current_col] == 'F' and [current_col, current_row] in pipe_locations:
                    mini_counter = 1
                    while True:
                        try:
                            mini_location = location_map[current_row + mini_counter][current_col]
                        except:
                            break
                        if mini_location == '|':
                            mini_counter += 1
                            continue
                        elif mini_location == 'L':
                            break
                        else:
                            jordan_counter += 1
                            break
                elif location_map[current_row][current_col] == '7' and [current_col, current_row] in pipe_locations:
                    mini_counter = 1
                    while True:
                        try:
                            mini_location = location_map[current_row + mini_counter][current_col]
                        except:
                            break
                        if mini_location == '|':
                            mini_counter += 1
                            continue
                        elif mini_location == 'J':
                            break
                        else:
                            jordan_counter += 1
                            break
            if jordan_counter % 2 != 0:
                enclosed_tiles += 1
    return enclosed_tiles

def replace_s_in_location_map(location_map, pipe_locations, pipe_map):
    pipe_map_1 = [pipe_locations[1][0] - pipe_locations[0][0], pipe_locations[1][1] - pipe_locations[0][1]]
    pipe_map_2 = [pipe_locations[-1][0] - pipe_locations[0][0] , pipe_locations[-1][1] - pipe_locations[0][1]]
    for str, directions in pipe_map:
        if pipe_map_1 in directions and pipe_map_2 in directions:
            s_replacement = str
    for row_idx, row in enumerate(location_map):
        for col_idx, cell in enumerate(row):
            if cell == 'S':
                location_map[row_idx][col_idx] = s_replacement
                return location_map
                    


def main():
    pipe_map = (
        ('-', [[1,0], [-1,0]]),
        ('|', [[0,1], [0,-1]]),
        ('7', [[-1,0], [0,1]]),
        ('L', [[0,-1], [1,0]]),
        ('F', [[0,1], [1,0]]),
        ('J', [[0,-1], [-1,0]])
    )
    file = "day-10-part-2/input.txt"
    location_map = generate_location_map(file)
    start_col, start_row = find_start_location(location_map)
    pipe_locations = generate_pipe_locations(location_map, pipe_map, start_col, start_row)
    location_map = replace_s_in_location_map(location_map, pipe_locations, pipe_map)
    enclosed_tiles = count_enclosed_tiles(location_map, pipe_locations)
    print(enclosed_tiles)

main()


# SUDO CODE
# pipe_map = (
#     ('-', [[1,0], [-1,0]]),
#     ('|', [[0,1], [0,-1]]),
#     ('7', [[-1,0], [0,1]]),
#     ('L', [[0,-1], [1,0]]),
#     ('F', [[0,1], [1,0]]),
#     ('J', [[0,-1], [-1,0]])
# )

# generate location_map from input.txt
# - i.e.
# location_map = (
#     ('.', '.', '.', '.', '.'),
#     ('.', 'S', '-', '7', '.'),
#     ('.', '|', '.', '|', '.'),
#     ('.', 'L', '-', 'J', '.'),
#     ('.', '.', '.', '.', '.')
# )


# find S location i.e. 1,1
# - for loop for each row
# - for loop for each column
# - exit loops when S found

# search for connecting pipe
# - s_location + [0, -1] i.e. [1 + 0, 1 - 1] = [1,0]. Check this is a valid location on location_map. Look at pipe_map for valid strs for [0, -1]
# -- is it valid str? i.e. No, it's '.'
# - s_location + [1, 0] i.e. [2,1]. Check this is a valid location on location_map. Look at pipe_map for valid strs for [1, 0]
# -- is it valid str? i.e. Yes, it's '-' then go to 'follow pipe' step
# - s_location + [0, 1] i.e. [1,2]. Check this is a valid location on location_map. Look at pipe_map for valid strs for [0, 1]
# -- is it valid str? i.e. Yes, it's '|' then go to 'follow pipe' step
# - s_location + [-1, 0] i.e. [0,1]. Check this is a valid location on location_map. Look at pipe_map for valid strs for [-1, 0]
# -- is it valid str? i.e. No, it's '.'

# follow pipe
# - look at pipe_map to determine next location
# '-' from [1, 0] goes [-1, 0] i.e. [4,2]. Check this is a valid location on location_map. 
# - is next location valid str? i.e. strs that have [-1, 0] in  pipe_map: '-', 'J','7'. Yes, it's '7' 
# loop over follow pipe until S location is reached or invalid str
# If invalid str reached then continue from 'search for connecting pipe' i.e. s_location + [0, 1]

# Once S location reached, find length of total strs/pipe
# - i.e. S, -, 7, |, J, -, L, | is 8
# - if even then divide by 2 i.e. 4
# - if odd then there are two answers: (divide by 2) + 1 and (divide by 2) - 1

# print final answer/s

# PART TWO

# generate the pipe_locations, which is a 1 if the location is part of the main loop pipe, and 0 if not i.e.

# pipe_locations = [
    # [1, 1], 
    # [2, 1], 
    # [3, 1], 
    # [4, 1], 
    # [4, 2], 
    # [4, 3], 
    # [3, 3], 
    # [2, 3], 
    # [1, 3], 
    # [1, 2]
# ]

# For each location in location_map that is not in value in pipe_locations:
# - go to the location below it i.e. [0,1]
# - if location is:
# -- is in pipe_locations and is '-', '7', 'J', 'F', 'L' then add 1 to counter and start again from 'go to the location below' with extra drop down e.g. [0,2], then [0,3]...
# -- is outside of the location_map then stop loop
# -- else again from 'go to the location below' with extra drop down e.g. [0,2], then [0,3]...
# if counter is odd then add 1 to tiles_enclosed. This takes advantage of the Jordan curve theorem.

# print tiles_enclosed
