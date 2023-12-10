import sys
from task import get_input

cards = get_input(sys.argv[1])

def parttwo():
    pile_total = 0
    for card in cards:
        card_total = 0
        start = 0
        for ch in range(8, len(card)):
            if card[ch] == '|':
                start = ch + 1
                break
        winners = [value for value in card[8:start-1].split(' ') if value]
        numbers = [value for value in card[start:].split(' ') if value]
        for number in numbers:
            if number in winners:
                if card_total == 0:
                    card_total = 1
                else:
                    card_total *= 2
        pile_total += card_total

    print(pile_total)


def partone():
    pile_total = 0
    for card in cards:
        card_total = 0
        start = 0
        for ch in range(8, len(card)):
            if card[ch] == '|':
                start = ch + 1
                break
        winners = [value for value in card[8:start-1].split(' ') if value]
        numbers = [value for value in card[start:].split(' ') if value]
        for number in numbers:
            if number in winners:
                if card_total == 0:
                    card_total = 1
                else:
                    card_total *= 2
        pile_total += card_total

    print(pile_total)
