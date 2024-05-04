import re

def parse_directions(file):
    with open(file, 'r') as file:
        string_file = file.read()
    
    sections = string_file.splitlines()
    directions = list(sections[0])
    clean_directions = []
    for direction in directions:
        if direction == 'R':
            clean_directions.append(1)
        elif direction == 'L':
            clean_directions.append(0)
        else:
            raise ValueError("Must be R or L")
    return clean_directions


def parse_map(file):
    with open(file, 'r') as file:
        string_file = file.read()
    
    sections = string_file.splitlines()
    map = {}
    
    for section in sections[2:]:
        map_key = section.split()[0]
        delimiters = r'[,() ]'
        map_L = re.split(delimiters, section)[-4]
        map_R = re.split(delimiters, section)[-2]
        map[map_key] = [map_L, map_R]

    return map


def main():

    file = "Input_test.txt"
    directions = parse_directions(file)
    map = parse_map(file)
    step = 0
    direction_step = 0
    key = 'AAA'
    while key != 'ZZZ':
        key = map[key][directions[direction_step]]
        step += 1
        if direction_step == len(directions) - 1:
            direction_step = 0
        else:
            direction_step += 1

    print(step)



main()


# {'aaa':['bbb','ccc']}
# RLLRR
# [1,0,0,1,1]