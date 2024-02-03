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
                    clean_hand.append(1)
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
    no_J_dict = {key: value for key, value in hand_dict.items() if key != 1}
    strength = 0
    if 0 == len(no_J_dict):
        strength = 7
        return strength
    elif 5 == max(no_J_dict.values()):
        strength = 7
    elif 4 == max(no_J_dict.values()):
        strength = 6
    elif 3 == max(no_J_dict.values()) and 2 in no_J_dict.values():
        strength = 5
    elif 3 == max(no_J_dict.values()):
        strength = 4
    elif 2 <= len([value for value in no_J_dict.values() if value == 2]):
        strength = 3
    elif 2 == max(no_J_dict.values()):
        strength = 2
    else:
        strength = 1
    
    if 1 in hand_dict:
        if strength == 6:
            strength = 7
        elif strength == 4:
            if hand_dict[1] == 2:
                strength = 7
            else:
                strength = 6
        elif strength == 3:
            strength = 5
        elif strength == 2:
            if hand_dict[1] == 3:
                strength = 7
            elif hand_dict[1] == 2:
                strength = 6
            else:
                strength = 4
        elif strength == 1:
            if hand_dict[1] == 5:
                strength = 7
            elif hand_dict[1] == 4:
                strength = 7
            elif hand_dict[1] == 3:
                strength = 6
            elif hand_dict[1] == 2:
                strength = 4
            else:
                strength = 2
    return strength


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
        # [bet, strngth, card 1, card 2, card 3, card 4, card 5]
    
    sorted_hands_details = sorted(hands_details, key=lambda x: (x[1], x[2], x[3], x[4], x[5], x[6]), reverse=True)

    multiply = len(sorted_hands_details)
    answer = 0
    for hand_details in sorted_hands_details:
        answer += multiply * hand_details[0]
        multiply -= 1

    print(answer)

main()
