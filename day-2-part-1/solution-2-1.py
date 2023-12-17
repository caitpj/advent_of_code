
def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    answer = 0
    game_results = {}

    for line in lines:
        games_str = line[8:].replace(':', '')
        id = int(line[5:8].replace(':', '').strip())
        result = is_possible(games_str, red=12, blue=14, green=13)
        game_results[id] = result

    for key, value in game_results.items():
        if value == True:
            answer += key

    print(game_results)
    print(answer)

def is_possible(games_str, red, blue, green):
    games = games_str.split(';')
    for game in games:
        colors = game.split(',')
        for color in colors:
            b_loc = color.find("blue")
            if b_loc != -1:
                count = int(color.split()[0])
                if count > blue:
                    return False
            r_loc = color.find("red")
            if r_loc != -1:
                count = int(color.split()[0])
                if count > red:
                    return False
            g_loc = color.find("green")
            if g_loc != -1:
                count = int(color.split()[0])
                if count > green:
                    return False
    return True


main()
