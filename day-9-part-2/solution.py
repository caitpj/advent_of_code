import re

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

    file = "day-9-part-2/input.txt"
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
    
    total_first_num_in_diff_list = []
    for full_diff_list in total_full_diff_list:
        first_num_in_diff_list = []
        for diff_list in full_diff_list:
            first_num_in_diff_list.append(diff_list[0])
        total_first_num_in_diff_list.append(first_num_in_diff_list)

    sum_prev_prediciton = 0
    for first_num_in_diff_list in total_first_num_in_diff_list:
        for i in range(len(first_num_in_diff_list) - 1):
            first_num_in_diff_list[i + 1]  = first_num_in_diff_list[i + 1] - first_num_in_diff_list[i]
        sum_prev_prediciton += first_num_in_diff_list[-1]
    print(sum_prev_prediciton)


main()
