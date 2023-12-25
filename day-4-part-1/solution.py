
from collections import Counter

def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    winning_numbers_list = []
    my_numbers_list = []

    answer = 0

    for line in lines:
        numbers = line.split(':')[1]
        winning_numbers = numbers.split('|')[0]
        my_numbers = numbers.split('|')[1]

        winning_numbers_list.append(winning_numbers.split())
        my_numbers_list.append(my_numbers.split())
    
    loop = 0
    for winning_numbers in winning_numbers_list:
        points = 0
        for winning_number in winning_numbers:
            for my_number in my_numbers_list[loop]:
                if my_number == winning_number:
                    if points == 0:
                        points = 1
                    else:
                        points = points*2
        answer += points
        loop += 1
    
    print(answer)


main()
