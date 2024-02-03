def parse_hands(file):
    with open(file, 'r') as file:
        string_file = file.read()
    
    sections = string_file.splitlines()
    hands_details = []
    for section in sections:
        hand = [*section.split()[0]]
        bet = int(section.split()[1])
        clean_hand = []
        for card in hand:
            try:
                clean_hand.append(int(card))
            except ValueError:
                if card == 'T':
                    clean_hand.append(10)
                elif card == 'J':
                    clean_hand.append(11)
                elif card == 'Q':
                    clean_hand.append(12)
                elif card == 'K':
                    clean_hand.append(13)
                elif card == 'A':
                    clean_hand.append(14)
                else:
                    raise ValueError("Must be a valid card")
        hands_details.append([clean_hand, bet])

    return hands_details


def hand_strength(hand):
    hand_dict = {i:hand.count(i) for i in hand}
    if 5 in hand_dict.values():
        return 7
    elif 4 in hand_dict.values():
        return 6
    elif 3 in hand_dict.values() and 2 in hand_dict.values():
        return 5
    elif 3 in hand_dict.values():
        return 4
    elif 2 <= len([value for value in hand_dict.values() if value == 2]):
        return 3
    elif 2 in hand_dict.values():
        return 2
    else:
        return 1


def main():

    hands_details = parse_hands("input.txt")
    for hand_details in hands_details:
        strength = hand_strength(hand_details[0])
        hand_details.append(strength)
        hand_details.append(hand_details[0][0])
        hand_details.append(hand_details[0][1])
        hand_details.append(hand_details[0][2])
        hand_details.append(hand_details[0][3])
        hand_details.append(hand_details[0][4])
        hand_details.pop(0) # no need for hand anymore, since we have everything we need
    
    sorted_hands_details = sorted(hands_details, key=lambda x: (x[1], x[2], x[3], x[4], x[5], x[6]), reverse=True)

    multiply = len(sorted_hands_details)
    answer = 0
    for hand_details in sorted_hands_details:
        answer += multiply * hand_details[0]
        multiply -= 1

    print(answer)



main()
