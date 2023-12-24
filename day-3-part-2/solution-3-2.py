
from collections import Counter

def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    coordinates_next_to_symbol = []
    coordinates_of_good_digit = []
    coordinate_of_left_most_digit = []
    correct_numbers = []
    correcter_numbers = []
    close_to_answer = []
    answer = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '*':
                coordinates_next_to_symbol.append([i, j+1, i, j])
                coordinates_next_to_symbol.append([i, j-1, i, j])
                coordinates_next_to_symbol.append([i+1, j, i, j])
                coordinates_next_to_symbol.append([i-1, j, i, j])
                coordinates_next_to_symbol.append([i+1, j+1, i, j])
                coordinates_next_to_symbol.append([i+1, j-1, i, j])
                coordinates_next_to_symbol.append([i-1, j+1, i, j])
                coordinates_next_to_symbol.append([i-1, j-1, i, j])

    for coordinate in coordinates_next_to_symbol:
        try:
            loc = lines[coordinate[0]][coordinate[1]]
        except IndexError:
            continue
        if loc.isdigit():
            coordinates_of_good_digit.append(coordinate)
    
    for coordinate in coordinates_of_good_digit:
        is_digit = True
        loop = 1
        while is_digit == True:
            if lines[coordinate[0]][coordinate[1] - loop].isdigit():
                loop += 1
            else:
                if [coordinate[0], coordinate[1] - loop + 1, coordinate[2], coordinate[3]] not in coordinate_of_left_most_digit:
                    coordinate_of_left_most_digit.append([coordinate[0], coordinate[1] - loop + 1, coordinate[2], coordinate[3]])
                is_digit = False

    for coordinate in coordinate_of_left_most_digit:
        string_num = lines[coordinate[0]][coordinate[1]]
        is_digit = True
        loop = 1
        while is_digit == True:
            if lines[coordinate[0]][coordinate[1] + loop].isdigit():
                string_num = string_num + lines[coordinate[0]][coordinate[1] + loop]
                loop += 1
            else:
                correct_numbers.append([int(string_num), str(coordinate[2])+','+str(coordinate[3])])
                is_digit = False

    counter = Counter()
    for correct_number in correct_numbers:
        counter[correct_number[1]] += 1

    for key, value in counter.items():
        if value == 2:
            correcter_numbers.append(key)
    
    for correcter_number in correcter_numbers:
        gear_ratio = 0
        for correct_number in correct_numbers:
            if correcter_number == correct_number[1]:
                if gear_ratio == 0:
                    gear_ratio = correct_number[0]
                else:
                    gear_ratio = gear_ratio * correct_number[0]
        close_to_answer.append(gear_ratio)
        
    for x in close_to_answer:
        answer += x
    
    print(answer)

main()
