def generate_map(file):
    with open(file, 'r') as file:
        map = list(list(line.strip()) for line in file)
    return map

def find_expanded_lines(map):
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
    
    return {'horizontal_lines_with_glalaxies': horizontal_lines_with_glalaxies,
            'vertical_lines_with_glalaxies': vertical_lines_with_glalaxies
            }

def main():
    file = "day-11-part-1/input.txt"
    map = generate_map(file)
    expanded_lines = find_expanded_lines(map)
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
    
    answer = 0
    for galaxy_idx, galaxy_location in enumerate(galaxy_locations):
        for i in range(len(galaxy_locations) - galaxy_idx - 1):
            x_galaxy_1 = galaxy_location[0]
            y_galaxy_1 = galaxy_location[1]
            x_galaxy_2 = galaxy_locations[i + galaxy_idx + 1][0]
            y_galaxy_2 = galaxy_locations[i + galaxy_idx + 1][1]
            answer += abs(x_galaxy_1 - x_galaxy_2)
            answer += abs(y_galaxy_1 - y_galaxy_2)
            for j in range(min([x_galaxy_1, x_galaxy_2]), max([x_galaxy_1, x_galaxy_2])):
                if j not in vertical_lines_with_glalaxies:
                    answer += 999999
            for j in range(min([y_galaxy_1, y_galaxy_2]), max([y_galaxy_1, y_galaxy_2])):
                if j not in horizontal_lines_with_glalaxies:
                    answer += 999999

    print(answer)

main()
