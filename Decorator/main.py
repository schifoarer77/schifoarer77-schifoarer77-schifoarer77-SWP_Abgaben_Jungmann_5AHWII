import random
import constants as con
import combinations as cmb
from decorator import timer


class card:
    def __init__(self, numerical_card, symbols):
        self.value = get_value(numerical_card, symbols)
        self.color = get_color(numerical_card, symbols)

    def __str__(self):
        if self.value == 11:
            tmp_str = 'J_'
        elif self.value == 12:
            tmp_str = 'Q_'
        elif self.value == 13:
            tmp_str = 'K_'
        elif self.value == 14:
            tmp_str = 'A_'
        else:
            tmp_str = f'{str(self.value)}_'

        if self.color == 0:
            tmp_str += con.CLUB
        elif self.color == 1:
            tmp_str += con.DIAMOND
        elif self.color == 2:
            tmp_str += con.HEART
        elif self.color == 3:
            tmp_str += con.SPADE
        else:
            tmp_str += str(self.color)

        return tmp_str


def get_color(numerical_card, symbols):
    return (numerical_card - 1) // symbols


def get_value(numerical_card, symbols):
    tmp_val = numerical_card % symbols
    # special cases
    if tmp_val == 0:  # when it's king
        return 13
    elif tmp_val == 1:  # when it's ace
        return 14
    return tmp_val

@timer
def init_cards(colors, symbols):
    # colors and symbols equal their quantities
    poker_cards = []
    for num in range(1, (colors * symbols) + 1):
        poker_cards.append(card(num, symbols))

    return poker_cards


def draw_cards(cards, total_draws):
    for i in range(total_draws):
        index = random.randint(0, (len(cards) - 1) - i)  # generate random index; card at that pos got selected
        # switch pos of selected number with number at the (now) last index
        cards[index], cards[(len(cards) - 1 - i)] = cards[(len(cards) - 1 - i)], cards[index]

    return cards[-total_draws:]


def check_combination(combinations_stat, cards):
    if cmb.royal_flush(cards):
        combinations_stat["royal_flush"] += 1
        print("royal flush")
    elif cmb.straight_flush(cards):
        combinations_stat["straight_flush"] += 1
        print("straight_flush")
    elif cmb.four_of_a_kind(cards):
        combinations_stat["four_of_a_kind"] += 1
        print("4 of a kind")
    elif cmb.full_house(cards):
        combinations_stat["full_house"] += 1
        print("full house")
    elif cmb.flush(cards):
        combinations_stat["flush"] += 1
        print("flush")
    elif cmb.straight(cards):
        combinations_stat["straight"] += 1
        print("straight")
    elif cmb.three_of_a_kind(cards):
        combinations_stat["three_of_a_kind"] += 1
        print("3 of a kind")
    elif cmb.two_pairs(cards):
        combinations_stat["two_pairs"] += 1
        print("2 pairs")
    elif cmb.pair(cards):
        combinations_stat["pair"] += 1
        print("pair")
    else:
        combinations_stat["high_card"] += 1
        print("high card")

    return combinations_stat


def print_statistics(actual, calculated):
    print("-------------------------------------------\nactual Statistics:\n")
    for comb_type in actual:
        print('%15s: %10.5f %%' % (comb_type, actual[comb_type]))
    # print(actual_statistics)

    print("-------------------------------------------\ncalculated Statistics:\n")
    for comb_type in calculated:
        percentage = (calculated[comb_type] / con.TOTAL_PLAYS) * 100
        calculated[comb_type] = percentage
        print('%15s: %10.5f %%' % (comb_type, percentage))
    # print(calculated_statistics)

    print("-------------------------------------------\ndifference:\n")
    for comb_type in calculated:
        difference = abs(calculated[comb_type] - actual[comb_type])
        print('%15s: %10.5f %%' % (comb_type, difference))


##############
# main
##############

@timer
def main():
    # initialize poker_cards
    poker_cards = init_cards(con.COLORS, con.SYMBOLS)

    # initialize dictionaries for statistics
    calculated_statistics = {
        'high_card': 0,
        'pair': 0,
        'two_pairs': 0,
        'three_of_a_kind': 0,
        'straight': 0,
        'flush': 0,
        'full_house': 0,
        'four_of_a_kind': 0,
        'straight_flush': 0,
        'royal_flush': 0
    }
    actual_statistics = {
        'high_card': 50.1177,
        'pair': 42.2569,
        'two_pairs': 4.7539,
        'three_of_a_kind': 2.1128,
        'straight': 0.3925,
        'flush': 0.1965,
        'full_house': 0.1441,
        'four_of_a_kind': 0.0240,
        'straight_flush': 0.00139,
        'royal_flush': 0.0000154
    }

    # actual game logic: draw cards, check combination, increase statistics-counter
    for i in range(con.TOTAL_PLAYS + 1):
        drawn_cards = draw_cards(poker_cards, con.DRAW_CARDS)

        # sort hand
        drawn_cards.sort(key=lambda c: c.value, reverse=False)

        # print hand cards
        output = ''
        for drawn_card in drawn_cards:
            output += f'{str(drawn_card)}, '

        print(output)

        # check for combination and increase it by 1
        calculated_statistics = check_combination(calculated_statistics, drawn_cards)

    # prepare and print statistics
    print_statistics(actual_statistics, calculated_statistics)


if __name__ == '__main__':
    main()

