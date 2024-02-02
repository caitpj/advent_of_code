def parse_races(races_file):
    with open(races_file, 'r') as file:
        string_file = file.read()
    
    sections = string_file.splitlines()
    race_times = sections[0].split()[1:]
    race_distances = sections[1].split()[1:]
    race_details = []
    for i in range(len(race_times)):
        race_details.append([int(race_times[i]), int(race_distances[i])])

    return race_details


def multiply_list(numbers):
    if not numbers:
        return 0
    result = 1
    for number in numbers:
        result *= number
    return result


def main():

    race_details = parse_races("input.txt")

    margin_of_errors = []
    for race_detail in race_details:
        margin_of_error = 0
        for i in range(race_detail[0]):
            if i * (race_detail[0] - i) > race_detail[1]:
                margin_of_error += 1
            elif margin_of_error > 0:
                break
        margin_of_errors.append(margin_of_error)

    answer = multiply_list(margin_of_errors)
    print(answer)


main()
