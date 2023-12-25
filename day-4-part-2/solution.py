
from collections import Counter

def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    winning_numbers_list = []
    my_numbers_list = []
    scratch_dict = {}

    answer = 0

    for line in lines:
        numbers = line.split(':')[1]
        winning_numbers = numbers.split('|')[0]
        my_numbers = numbers.split('|')[1]

        winning_numbers_list.append(winning_numbers.split())
        my_numbers_list.append(my_numbers.split())
    
    loop = 0
    for winning_numbers in winning_numbers_list:
        matches = 0
        try:
            scratch_dict[loop + 1 + matches] += 1
        except KeyError:
            scratch_dict[loop + 1 + matches] = 1
        for winning_number in winning_numbers:
            for my_number in my_numbers_list[loop]:
                if my_number == winning_number:
                    matches += 1
                    try:
                        scratch_dict[loop + 1 + matches] += scratch_dict[loop + 1]
                    except KeyError:
                        scratch_dict[loop + 1 + matches] = scratch_dict[loop + 1]
        loop += 1
    
    for scratch in scratch_dict:
        answer += scratch_dict[scratch]
    
    print(answer)


main()
