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

    file = "day-8-part-2/input.txt"
    directions = parse_directions(file)
    map = parse_map(file)

    direction_step = 0
    stage = []
    for key, value in map.items():
        stage_n = []
        if key[-1] == 'A':
            stage_n.append(key)
            stage_n.append(value[0])
            stage_n.append(value[1])
            stage.append(stage_n)

    complete = []
    for i in range(len(stage)):
        complete.append(False)

    for stage_n in stage:
        steps = 0
        true_count = 0
        while true_count < 1:
            for i in range(len(complete)):
                complete[i] = False
            stage_loop = 0
            direction = directions[direction_step]
            next_step_key = stage_n[direction + 1]
            stage_n = []
            stage_n.append(next_step_key)
            stage_n.append(map[next_step_key][0])
            stage_n.append(map[next_step_key][1])
            stage[stage_loop] = stage_n
            stage_loop += 1        
            steps += 1
            direction_step += 1
            if direction_step == len(directions):
                direction_step = 0
            if stage_n[0][-1] == 'Z':
                complete[stage_loop] = True
                true_count += 1
                print(steps)
    # with the values printed, you can find the least common multiple of them at https://www.calculatorsoup.com/calculators/math/lcm.php


main()


# {'aaa':['bbb','ccc']}
# RLLRR
# [1,0,0,1,1]