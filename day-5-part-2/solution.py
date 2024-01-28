def seed_ranger(map_str):
    seed_ranges = []
    level = 1
    sections = map_str.split("\n\n")
    seeds = sections[0][6:].split()
    for i in range(0,len(seeds), 2):
        min_range = int(seeds[i])
        max_range = int(seeds[i+1]) + min_range - 1
        seed_range = [min_range, max_range, level]
        seed_ranges.append(seed_range)
    return seed_ranges

def parse_map(map_str):
    sections = map_str.split("\n\n")
    level = 1
    maps = {}
    for section in sections[1:]:    
        _, *map_lines = section.splitlines()
        fmt_map_lines = []
        for map_line in map_lines:
            range_start = int(map_line.split(' ')[1])
            range_end = int(map_line.split(' ')[1]) + int(map_line.split(' ')[2]) - 1
            transformation = int(map_line.split(' ')[0]) - int(map_line.split(' ')[1])
            fmt_map_line = [range_start, range_end, transformation]
            fmt_map_lines.append(fmt_map_line)
        maps[level] = fmt_map_lines
        level += 1
    return maps

def main():

    with open("input.txt", 'r') as file:
        string_file = file.read()
    
    my_maps = parse_map(string_file)
    my_seed_ranges = seed_ranger(string_file)
    min_location = float('inf')
    max_level = 7

    for my_seed_range in my_seed_ranges:
        level = my_seed_range[2]
        min_seed_range = my_seed_range[0]
        max_seed_range = my_seed_range[1]
        made_it = False
        
        for min_map, max_map, transform in my_maps[level]:
            if min_seed_range > max_map or max_seed_range < min_map:
                continue

            elif min_seed_range >= min_map and max_seed_range <= max_map:
                min_seed_range = min_seed_range + transform
                max_seed_range = max_seed_range + transform
                if level == max_level:
                    min_location = min(min_location, min_seed_range)
                else:
                    my_seed_ranges.append([min_seed_range, max_seed_range, level + 1])
                made_it = True
                break

            elif min_seed_range > min_map and max_seed_range > max_map:
                my_seed_ranges.append([min_seed_range, max_map, level])
                my_seed_ranges.append([max_map + 1, max_seed_range, level])
                made_it = True
                break
            elif min_seed_range < min_map and max_seed_range < max_map:
                my_seed_ranges.append([min_seed_range, min_map - 1, level])
                my_seed_ranges.append([min_map, max_seed_range, level])
                made_it = True
                break
            elif min_seed_range < min_map and max_seed_range > max_map:
                my_seed_ranges.append([min_seed_range, min_map - 1, level])
                my_seed_ranges.append([min_map, max_map, level])
                my_seed_ranges.append([max_map + 1, max_seed_range, level]) 
                made_it = True
                break     
        
        if made_it == False and level == max_level:
            min_location = min(min_location, min_seed_range)
        elif made_it == False:
            my_seed_ranges.append([min_seed_range, max_seed_range, level + 1])

    print(min_location)


main()
