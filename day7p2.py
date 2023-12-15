hands = []

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []
sorted_five_of_a_kind = []
sorted_four_of_a_kind = []
sorted_full_house = []
sorted_three_of_a_kind = []
sorted_two_pair = []
sorted_one_pair = []
sorted_high_card = []

card_rank_dict = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 0,
    'Q': 11,
    'K': 12,
    'A': 13}


def process_hand_with_jacks(hand):
    cards = [1, 0, 0, 0, 0]
    #
    for index, card in enumerate(hand[0][1:], 1):
        found = False
        for index2 in range(0, index):
            if hand[0][index] == hand[0][index2]:
                cards[index2] += 1
                found = True
                break
        if not found:
            cards[index] += 1
    cards.sort(reverse=True)

    num_jacks = hand[0].count('J')

    if cards[0] == 5:
        five_of_a_kind.append(hand)
    elif cards[0] == 4:
        if num_jacks == 1 or num_jacks == 4:
            # Jack converts four of a kind to five of a kind.
            five_of_a_kind.append(hand)
        else:
            four_of_a_kind.append(hand)
    elif cards[0] == 3:
        if cards[1] == 2:
            if num_jacks > 0:
                # Jacks convert full house to five of a kind
                five_of_a_kind.append(hand)
            else:
                full_house.append(hand)
        else:
            if num_jacks == 2:
                # 2 Jacks convert three of a kind to five of a kind
                five_of_a_kind.append(hand)
            elif num_jacks == 1 or num_jacks == 3:
                # 1 or 3 Jacks convert three of a kind to four of a kind
                four_of_a_kind.append(hand)
            else:
                three_of_a_kind.append(hand)
    elif cards[0] == 2:
        if cards[1] == 2:
            if num_jacks == 2:
                # 2 Jacks convert two pair to four of a kind
                four_of_a_kind.append(hand)
            elif num_jacks == 1:
                # 1 Jack converts two pair to full house
                full_house.append(hand)
            else:
                two_pair.append(hand)
        else:
            if num_jacks > 0:
                # 1 or 2 Jack converts pair into three of a kind
                three_of_a_kind.append(hand)
            else:
                one_pair.append(hand)
    else:
        if num_jacks == 1:
            # one Jack converts high into pair
            one_pair.append(hand)
        else:
            high_card.append(hand)

    return


def process_hand(hand):
    cards = [1, 0, 0, 0, 0]

    for index, card in enumerate(hand[0][1:], 1):
        found = False
        for index2 in range(0, index):
            if (hand[0][index] == hand[0][index2]):
                cards[index2] += 1
                found = True
                break
        if not found:
            cards[index] += 1
    cards.sort(reverse=True)

    if cards[0] == 5:
        five_of_a_kind.append(hand)
    elif cards[0] == 4:
        four_of_a_kind.append(hand)
    elif cards[0] == 3:
        if cards[1] == 2:
            full_house.append(hand)
        else:
            three_of_a_kind.append(hand)
    elif cards[0] == 2:
        if cards[1] == 2:
            two_pair.append(hand)
        else:
            one_pair.append(hand)
    else:
        high_card.append(hand)

    return


def print_hands():
    print("Unsorted")
    print("Five of a kind:", five_of_a_kind)
    print("Four of a kind:", four_of_a_kind)
    print("Full house:", full_house)
    print("Three of a kind:", three_of_a_kind)
    print("Two pair:", two_pair)
    print("One pair:", one_pair)
    print("High card", high_card)


def print_sorted_hands():
    print("Sorted")
    print("Five of a kind:", sorted_five_of_a_kind)
    print("Four of a kind:", sorted_four_of_a_kind)
    print("Full house:", sorted_full_house)
    print("Three of a kind:", sorted_three_of_a_kind)
    print("Two pair:", sorted_two_pair)
    print("One pair:", sorted_one_pair)
    print("High card", sorted_high_card)


def a_less_than_b(hand_a, hand_b):

    for index in range(0, len(hand_a[0])):
        # if both are digits, or a is digit and b is letter, then simple less than works.
        # if both are characters then need to be more clever
        if card_rank_dict[hand_a[0][index]] < card_rank_dict[hand_b[0][index]]:
            return True
        elif card_rank_dict[hand_a[0][index]] > card_rank_dict[hand_b[0][index]]:
            return False

    return True


def sort_hands(hands):
    sorted_hands = []
    for hand in hands:
        inserted = False
        for index, sorted_hand in enumerate(sorted_hands):
            if a_less_than_b(hand, sorted_hand):
                sorted_hands.insert(index, hand)
                inserted = True
                break
        if not inserted:
            sorted_hands.append(hand)
    return sorted_hands


def calculate_score():
    rank = 1
    score = 0
    for hand in sorted_high_card:
        score += rank * hand[1]
        rank += 1

    for hand in sorted_one_pair:
        score += rank * hand[1]
        rank += 1

    for hand in sorted_two_pair:
        score += rank * hand[1]
        rank += 1

    for hand in sorted_three_of_a_kind:
        score += rank * hand[1]
        rank += 1

    for hand in sorted_full_house:
        score += rank * hand[1]
        rank += 1

    for hand in sorted_four_of_a_kind:
        score += rank * hand[1]
        rank += 1

    for hand in sorted_five_of_a_kind:
        score += rank * hand[1]
        rank += 1

    return score

with open("input7.txt") as my_file:
    # Read in hands and store by type of hand
    for line in my_file:
        hands.append((line.split()[0], int(line.split()[1])))
        process_hand_with_jacks(hands[-1])

    # Sort each type of hand based on card ordering rules
    sorted_five_of_a_kind = sort_hands(five_of_a_kind)
    sorted_four_of_a_kind = sort_hands(four_of_a_kind)
    sorted_full_house = sort_hands(full_house)
    sorted_three_of_a_kind = sort_hands(three_of_a_kind)
    sorted_two_pair = sort_hands(two_pair)
    sorted_one_pair = sort_hands(one_pair)
    sorted_high_card = sort_hands(high_card)

    print_hands()
    print_sorted_hands()

    # calculate score
    score = calculate_score()
    print(score)