def parse_histories(file):
    with open(file, 'r') as file:
        string_file = file.read()
    
    sections = string_file.splitlines()
    histories = []
    for section in sections:
        history = section.split(' ')
        history = [ int(x) for x in history ]
        histories.append(history)

    return histories


def main():

    file = "day-9-part-1/input.txt"
    histories = parse_histories(file)
    total_full_diff_list = []

    for history in histories:
        current_level = history
        full_diff_list = [history]
        loops = len(history) - 1
        for i in range(loops):
            next_level = []
            for j in range(loops - i):
                diff = current_level[j + 1] - current_level[j]
                next_level.append(diff)
            full_diff_list.append(next_level)
            current_level = next_level
            reverse_full_diff_list = full_diff_list[::-1]
        total_full_diff_list.append(reverse_full_diff_list)
    
    total_final_num_in_diff_list = []
    for full_diff_list in total_full_diff_list:
        final_num_in_diff_list = []
        for diff_list in full_diff_list:
            final_num_in_diff_list.append(diff_list[-1])
        total_final_num_in_diff_list.append(final_num_in_diff_list)

    total_sum = sum(sum(final_num_in_diff_list) for final_num_in_diff_list in total_final_num_in_diff_list)
    print(total_sum)


main()
