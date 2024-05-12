def generate_map(file):
    with open(file, 'r') as file:
        map = list(list(line.strip()) for line in file)
    return map

def expand_map(map):
    galaxy_locations = []
    for line_idx, line in enumerate(map):
        for cell_idx, cell in enumerate(line):
            if cell != '#':
                continue    
            galaxy_locations.append([cell_idx, line_idx])

    horizontal_lines_with_glalaxies = set()
    vertical_lines_with_glalaxies = set()
    for location in galaxy_locations:
        horizontal_lines_with_glalaxies.add(location[1])
        vertical_lines_with_glalaxies.add(location[0])
    
    len_map = len(map)
    len_line = len(map[0])
    for line_idx in range(len_map):
        new_line = []
        for cell_idx in range(len_line):
            new_line.append(map[line_idx][cell_idx])
            if cell_idx not in vertical_lines_with_glalaxies:
                new_line.append('.')
        map[line_idx] = new_line
    
    new_line = len(map[0]) * ['.']
    for line_idx in range(len_map - 1, -1, -1):    
        if line_idx not in horizontal_lines_with_glalaxies:
            map.insert(line_idx, new_line)
    return map


def main():
    file = "day-11-part-1/input.txt"
    map = generate_map(file)
    expanded_map = expand_map(map)
    
    galaxy_locations = []
    for line_idx, line in enumerate(expanded_map):
        for cell_idx, cell in enumerate(line):
            if cell != '#':
                continue    
            galaxy_locations.append([cell_idx, line_idx])
    
    answer = 0
    for galaxy_idx, galaxy_location in enumerate(galaxy_locations):
        for i in range(len(galaxy_locations) - galaxy_idx - 1):
            answer += abs(galaxy_location[0] - galaxy_locations[i + galaxy_idx + 1][0])
            answer += abs(galaxy_location[1] - galaxy_locations[i + galaxy_idx + 1][1])

    print(answer)

main()
