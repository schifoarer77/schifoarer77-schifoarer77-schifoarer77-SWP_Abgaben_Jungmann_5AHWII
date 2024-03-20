
def royal_flush(cards):
    # 1. check for being a straight_flush
    if straight_flush(cards):
        # highest possible straights starts with a 10
        return cards[0].value == 10

    return False


def straight_flush(cards):
    # 1. check for being a flush
    if flush(cards):
        # 2. check for being a straight
        if straight(cards):
            return True

    return False


def four_of_a_kind(cards):
    for selected_card in cards[:2]:
        same_value = 0
        for compare_card in cards:
            if selected_card.value == compare_card.value:
                same_value += 1

        if same_value == 4:
            return True

    return False

    # check for being a 4 of a kind
    return cards_match_base == 4


def full_house(cards):
    # full house is a combination of one pair and one three-of-a-kind
    # 1. check for containing a three of a kind
    if three_of_a_kind(cards):
        # 2. check for containing a pair
        if pair(cards):
            return True

    return False


def straight(cards):
    # special case: a street can start with an ace. has to continue with 2, 3, 4, 5
    if cards[0].value == 14:
        match_list = [2, 3, 4, 5]
        for i in range(len(cards) - 2):
            if cards[1 + i].value != match_list[i]:
                return False

        return True

    # every following card must be one value higher than the previous
    for i in range(len(cards) - 1):
        if cards[i].value != cards[i + 1].value - 1:
            return False

    return True


def flush(cards):
    color = cards[0].color
    for sel_card in cards[1:]:
        if color != sel_card.color:
            return False

    return True


def three_of_a_kind(cards):
    for sel_card in cards:
        same_value = 0
        for compare_card in cards:
            if sel_card.value == compare_card.value:
                same_value += 1

        if same_value == 3:
            return True

    return False


def two_pairs(cards):
    num_of_cards_of_pairs = 0
    for sel_card in cards:
        same_value = 0
        for compare_card in cards:
            if sel_card.value == compare_card.value:
                same_value += 1

        # a pair has 2 cards, so this gets called twice per pair
        if same_value == 2:
            num_of_cards_of_pairs += 1

        # if 4 cards belong to pairs, there's a total of 2 pairs
        if num_of_cards_of_pairs == 4:
            return True

    return False


def pair(cards):
    for sel_card in cards:
        same_value = 0
        for compare_card in cards:
            if sel_card.value == compare_card.value:
                same_value += 1

        if same_value == 2:
            return True

    return False

