import random
import matplotlib.pyplot as plt

count_color = 4
count_symbols = 13

#Erstellt eine Liste von Karten mit allen möglichen Kartenkombinationen von Farben und Symbolen.
def create_cards():
    return [a for a in range(count_color * count_symbols)]

#Zieht bestimmte Anzahl von Karten aus gegebenen Liste zufällig,
#   indem sie die random.sample-Funktion verwendet.
def get_cards(lst, numbers_to_draw):
    return random.sample(lst, numbers_to_draw)

#Teilt die Karten in Symbole und Farben auf und gibt zwei separate Listen zurück.
def get_symbol_and_color(cards):
    return [card % count_symbols for card in cards], [card // count_symbols for card in cards]

#Überprüft, ob eine gegebene Liste von Karten eine bestimmte Anzahl von Vorkommen eines Werts aufweist.
def has_occurrences(cards, n):
    return any(cards.count(value) == n for value in set(cards))

#Überprüft, ob die Karten eine Flush-Kombination (alle Karten der gleichen Farbe) aufweisen,
#   indem sie die Farben überprüft.
def is_flush(cards):
    colors = get_symbol_and_color(cards)[1]
    return has_occurrences(colors, 5)

#Überprüft, ob die Karten eine Straight-Kombination (aufeinanderfolgende Symbole) aufweisen,
#   indem sie die Symbole sortiert und auf Muster überprüft.
def is_straight(cards):
    symbols = get_symbol_and_color(cards)[0]
    return sorted(symbols) in [{0, 9, 10, 11, 12}] + [list(range(i, i+5)) for i in range(9)]

#Überprüft die Kombination der gegebenen Karten und aktualisiert
#   ein Dictionary (dic) mit den gefundenen Kombinationen.
def check_combination(cards, dic):
    if is_flush(cards) and is_straight(cards):
        dic["Royal Flush" if 0 in get_symbol_and_color(cards)[0] else "Straight Flush"] += 1
    elif has_occurrences(cards, 4):
        dic["Four of a kind"] += 1
    elif has_occurrences(cards, 3) and has_occurrences(cards, 2):
        dic["Full House"] += 1
    elif is_flush(cards):
        dic["Flush"] += 1
    elif is_straight(cards):
        dic["Straight"] += 1
    elif has_occurrences(cards, 3):
        dic["Three of a kind"] += 1
    elif has_occurrences(cards, 2) == 2:
        dic["Two Pair"] += 1
    elif has_occurrences(cards, 2):
        dic["Pair"] += 1
    else:
        dic["High Card"] += 1

#Führt eine Testreihe durch, um die Wahrscheinlichkeiten verschiedener Kombinationen zu ermitteln.
#   Sie erstellt ein Dictionary (propability), das die Wahrscheinlichkeiten speichert
#   und erstellt schließlich ein Tortendiagramm (Pie-Chart) mithilfe von Matplotlib,
#   um die Ergebnisse anzuzeigen.
def execute_testing(count=1):
    dic = {
        "Royal Flush": 0,
        "Straight Flush": 0,
        "Four of a kind": 0,
        "Full House": 0,
        "Flush": 0,
        "Straight": 0,
        "Three of a kind": 0,
        "Two Pair": 0,
        "Pair": 0,
        "High Card": 0
    }
    propability = {key: 0 for key in dic}

    for _ in range(count):
        check_combination(get_cards(create_cards(), 5), dic)

    print(dic)

    for key in propability:
        propability[key] = (dic[key] / count) * 100

    print(propability)

    ax = plt.subplot()
    ax.pie(list(propability.values()), labels=list(propability.keys()), autopct="%1.5f%%", radius=1.3)
    plt.show()

execute_testing(1_000_000)
