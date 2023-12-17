# import str


def main():
    file1 = open("input.txt", "r")
    lines = file1.readlines()
    answer = 0

    for line in lines:
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
