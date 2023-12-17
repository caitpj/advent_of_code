
def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    answer = 0
    game_results = {}

    for line in lines:
        games_str = line[8:].replace(':', '')
        result = fewest_cubes(games_str)
        answer += result['red'] * result['blue'] * result['green']

    print(answer)

def fewest_cubes(games_str):
    games = games_str.split(';')
    output = {'red': 0, 'blue': 0, 'green': 0}
    for game in games:
        colors = game.split(',')
        for color in colors:
            b_loc = color.find("blue")
            if b_loc != -1:
                count = int(color.split()[0])
                if count > output['blue']:
                    output['blue'] = count
            r_loc = color.find("red")
            if r_loc != -1:
                count = int(color.split()[0])
                if count > output['red']:
                    output['red'] = count
            g_loc = color.find("green")
            if g_loc != -1:
                count = int(color.split()[0])
                if count > output['green']:
                    output['green'] = count
    return output


main()
