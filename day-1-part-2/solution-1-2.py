
def main():
    file1 = open("input.txt", "r")
    lines = file1.readlines()
    answer = 0
    text_num = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for line in lines:
        for key, value in text_num.items():
            if key in line:
                line = line.replace(key, key + value + key)

        first = first_digit(line)
        last = last_digit(line)
        callibration = int(first + last)
        answer += callibration

    print(answer)


def first_digit(x):
    for char in x:
        if char.isdigit():
            return char


def last_digit(x):
    for char in x[::-1]:
        if char.isdigit():
            return char


main()
