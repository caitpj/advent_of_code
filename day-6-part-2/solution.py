def parse_races(races_file):
    with open(races_file, 'r') as file:
        string_file = file.read()
    
    sections = string_file.splitlines()
    race_times = ''.join(sections[0].split()[1:])
    race_distances = ''.join(sections[1].split()[1:])
    race_details = [int(race_times), int(race_distances)]

    return race_details


def main():

    race_details = parse_races("input.txt")

    margin_of_error = 0
    for i in range(race_details[0]):
        if i * (race_details[0] - i) > race_details[1]:
            margin_of_error += 1
        elif margin_of_error > 0:
            break

    print(margin_of_error)


main()
