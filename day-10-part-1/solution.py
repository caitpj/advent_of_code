def find_start_location(location_map):
    for row_idx, row in enumerate(location_map):
        for col_idx, cell in enumerate(row):
            if cell == 'S':
                return col_idx, row_idx
    return None

def is_valid_location(location_map, col, row):
    num_rows = len(location_map)
    num_cols = len(location_map[0])
    return 0 <= row < num_rows and 0 <= col < num_cols

def follow_pipe(location_map, pipe_map, start_col, start_row):
    direction_attempts = [[1,0], [0,1], [-1,0], [0,-1]]
    current_row, current_col = start_row, start_col
    
    for direction_attempt in direction_attempts:
        current_direction = direction_attempt
        current_row = current_row + current_direction[1]
        current_col = current_col + current_direction[0]
        pipe_length = 0
        loop = True
        while loop:
            pipe_checks = 0
            for pipe, directions in pipe_map:
                if location_map[current_row][current_col] != pipe:
                    pipe_checks += 1
                    if pipe_checks == 6:
                        loop = False
                        break
                    continue
                pipe_length += 1
                for direction in directions:
                    if direction == [current_direction[0] * (-1), current_direction[1] * (-1)]:
                        continue
                    current_direction = direction
                    next_col = current_col + current_direction[0]
                    next_row = current_row + current_direction[1]
                    if not is_valid_location(location_map, next_row, next_col):
                        loop = False
                        break
                    if location_map[next_row][next_col] == 'S':
                        pipe_length += 1
                        return pipe_length
                    current_row, current_col = next_row, next_col
                    break

def find_pipe_length(location_map, pipe_map):
    start_col, start_row = find_start_location(location_map)
    if start_row is None:
        return "Start location 'S' not found."
    
    pipe_length = follow_pipe(location_map, pipe_map, start_col, start_row)
    
    if pipe_length is None:
        return "No valid pipe found from start location 'S'."
    else:
        if pipe_length % 2 == 0:
            return pipe_length // 2
        else:
            return (pipe_length // 2) + 1, (pipe_length // 2) - 1

def generate_location_map(file):
    with open(file, 'r') as file:
        location_map = tuple(tuple(line.strip()) for line in file)
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
    file = "day-10-part-1/input.txt"
    location_map = generate_location_map(file)

    result = find_pipe_length(location_map, pipe_map)
    print(result)

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