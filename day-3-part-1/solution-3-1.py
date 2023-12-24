
def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    coordinates_next_to_symbol = []
    coordinates_of_good_digit = []
    coordinate_of_left_most_digit = []
    correct_numbers = []
    answer = 0

    for i in range(len(lines) -1):
        for j in range(len(lines[i]) -1):
            if not lines[i][j].isalnum() and lines[i][j] not in ('.', '\\'):
                coordinates_next_to_symbol.append([i, j+1])
                coordinates_next_to_symbol.append([i, j-1])
                coordinates_next_to_symbol.append([i+1, j])
                coordinates_next_to_symbol.append([i-1, j])
                coordinates_next_to_symbol.append([i+1, j+1])
                coordinates_next_to_symbol.append([i+1, j-1])
                coordinates_next_to_symbol.append([i-1, j+1])
                coordinates_next_to_symbol.append([i-1, j-1])
    
    for coordinate in coordinates_next_to_symbol:
        try:
            loc = lines[coordinate[0]][coordinate[1]]
        except IndexError:
            continue
        if loc.isdigit():
            coordinates_of_good_digit.append([coordinate[0], coordinate[1]])
    
    for coordinate in coordinates_of_good_digit:
        is_digit = True
        loop = 1
        while is_digit == True:
            if lines[coordinate[0]][coordinate[1] - loop].isdigit():
                loop += 1
            else:
                if [coordinate[0], coordinate[1] - loop + 1] not in coordinate_of_left_most_digit:
                    coordinate_of_left_most_digit.append([coordinate[0], coordinate[1] - loop + 1])
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
                correct_numbers.append(int(string_num))
                is_digit = False

    for correct_number in correct_numbers:
        answer += correct_number

    print(answer)

main()
