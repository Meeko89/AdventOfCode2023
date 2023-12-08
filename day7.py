
hand_types = {}


def get_strength(hand: str, joker=False) -> int:
    hand_values = {
        "five-of-a-kind": "7",
        "four-of-a-kind": "6",
        "full-house": "5",
        "three-of-a-kind": "4",
        "two-pair": "3",
        "one-pair": "2",
        "high-card": "1"
    }
    card_values = {
        "2": "02",
        "3": "03",
        "4": "04",
        "5": "05",
        "6": "06",
        "7": "07",
        "8": "08",
        "9": "09",
        "T": "10",
        "J": "01" if joker else "11",
        "Q": "12",
        "K": "13",
        "A": "14"
    }

    cards_in_hand = {}
    for card in hand:
        cards_in_hand[card] = hand.count(card)

    strength = ""
    card_counts = list(cards_in_hand.values())
    jokers_in_hand = cards_in_hand["J"] if ("J" in cards_in_hand.keys()) else 0

    print(sorted(hand), end=", ")
    if joker:
        print("-".join(sorted([c * x for (c, x) in cards_in_hand.items() if c != "J"])), end=", ")
        if jokers_in_hand > 0:
            print("-".join([c * x for (c, x) in cards_in_hand.items() if c == "J"]), end=", ")
        print([x for (c, x) in cards_in_hand.items() if c != "J"], end=", ")
        if jokers_in_hand > 0:
            print(f"[{jokers_in_hand}]", end=", ")
    else:
        print(card_counts, end=", ")

    f = jokers_in_hand + max([x for x in cards_in_hand.values() if x != "J"])
    max_others = max([x for (c, x) in cards_in_hand.items() if c != "J"]) if jokers_in_hand != 5 else 0
    if (card_counts.count(5) > 0 or
            (joker and jokers_in_hand + max_others >= 5)):
        strength += hand_values["five-of-a-kind"]
        if 5 in hand_types:
            hand_types[5].append(sorted(hand))
        else:
            hand_types[5] = [sorted(hand)]
        print("five-of-a-kind", end=", ")

    if (strength == "" and
            (card_counts.count(4) > 0 or
             (joker and jokers_in_hand + max([x for (c, x) in cards_in_hand.items() if c != "J"]) >= 4))):
        strength += hand_values["four-of-a-kind"]
        print("four-of-a-kind", end=", ")
        typ = 4
        if typ in hand_types:
            hand_types[typ].append(sorted(hand))
        else:
            hand_types[typ] = [sorted(hand)]

    if strength == "":
        if card_counts.count(3) > 0 and card_counts.count(2) > 0:
            strength += hand_values["full-house"]
            typ = 32
            if typ in hand_types:
                hand_types[typ].append(sorted(hand))
            else:
                hand_types[typ] = [sorted(hand)]
            print("full-house", end=", ")
        elif joker:
            for (card, amount) in cards_in_hand.items():
                other_cards = [x for (c, x) in cards_in_hand.items() if (c != "J" and c != card)]
                max_other = max([x for (c, x) in cards_in_hand.items() if (c != "J" and c != card)])
                if (card != "J" and
                        ((amount == 3 and max_other + jokers_in_hand >= 2) or
                         (amount == 2 and max_other + jokers_in_hand >= 3) or
                         (amount == 2 and jokers_in_hand >= 1 and max_other + jokers_in_hand - 1 >= 2) or
                         (amount == 1 and jokers_in_hand >= 2 and max_other + jokers_in_hand - 2 >= 2) or
                         (amount == 1 and jokers_in_hand >= 1 and max_other + jokers_in_hand - 1 >= 3))):
                    strength += hand_values["full-house"]
                    typ = 32
                    if typ in hand_types:
                        hand_types[typ].append(sorted(hand))
                    else:
                        hand_types[typ] = [sorted(hand)]
                    print("full-house", end=", ")
                    break

    if strength == "":
        max_other = max([x for (c, x) in cards_in_hand.items() if c != "J"])
        if card_counts.count(3) > 0:
            strength += hand_values["three-of-a-kind"]
            typ = 3
            if typ in hand_types:
                hand_types[typ].append(sorted(hand))
            else:
                hand_types[typ] = [sorted(hand)]
            print("three-of-a-kind", end=", ")
        elif joker and max_other + jokers_in_hand >= 3:
            strength += hand_values["three-of-a-kind"]
            typ = 3
            if typ in hand_types:
                hand_types[typ].append(sorted(hand))
            else:
                hand_types[typ] = [sorted(hand)]
            print("three-of-a-kind", end=", ")

    if strength == "":
        max_other = max([x for x in cards_in_hand.values() if x != "J"])
        if card_counts.count(2) > 1:
            typ = 2
            if typ in hand_types:
                hand_types[typ].append(sorted(hand))
            else:
                hand_types[typ] = [sorted(hand)]
            strength += hand_values["two-pair"]
            print("two-pair", end=", ")
        elif joker and (jokers_in_hand >= 2 or max_other >= 2 and jokers_in_hand >= 1):
            strength += hand_values["two-pair"]
            typ = 2
            if typ in hand_types:
                hand_types[typ].append(sorted(hand))
            else:
                hand_types[typ] = [sorted(hand)]
            print("two-pair", end=", ")

    if strength == "":
        if card_counts.count(2) > 0:
            strength += hand_values["one-pair"]
            typ = 1
            if typ in hand_types:
                hand_types[typ].append(sorted(hand))
            else:
                hand_types[typ] = [sorted(hand)]
            print("one-pair", end=", ")
        elif joker and (jokers_in_hand >= 1):
            strength += hand_values["one-pair"]
            typ = 1
            if typ in hand_types:
                hand_types[typ].append(sorted(hand))
            else:
                hand_types[typ] = [sorted(hand)]
            print("one-pair", end=", ")

    if strength == "":
        strength += hand_values["high-card"]
        typ = 0
        if typ in hand_types:
            hand_types[typ].append(sorted(hand))
        else:
            hand_types[typ] = [sorted(hand)]
        print("high-card", end=", ")

    print(strength, end=", ")
    for card in hand:
        strength += card_values[card]

    if joker and jokers_in_hand == 1:
        print(strength, end="")
    elif joker and jokers_in_hand == 2:
        print(strength, end="")
    elif joker and jokers_in_hand == 4:
        print(strength, end="")
    elif joker and jokers_in_hand == 5:
        print(strength, end="")

    else:
        print(strength, end="")
    print()
    return int(strength, 10)


if __name__ == '__main__':
    testing_hands = [
        ("J5JJ5", "7"),
        ("4QJQ4", "5"),
        ("JJJ6Q", "6"),
        ("JJ6K4", "4")
    ]
    for (h, typ) in testing_hands:
        s = get_strength(h, True)
        if str(s)[0] != typ:
            print(get_strength(h, True), "!=", typ)
            exit()

    files = ["input_data/day7_example1.txt", "input_data/day7.txt"]

    for file in files:
        with open(file, 'r') as f:
            data = f.readlines()

        hands = []
        for row in data:
            splits = row.split(" ")
            hand = splits[0]
            bid = int(splits[1])
            typ = ""
            if len(splits) == 3:
                typ = row.split(" ")[2].strip()
                print(typ)

            hands.append({"hand": hand, "bid": bid, "typ": typ})

        hands.sort(key=lambda x: get_strength(x["hand"], joker=False))

        total_winnings = 0
        for i in range(len(hands)):
            total_winnings += hands[i]["bid"] * (i+1)

        print()
        hand_types = {}
        hands.sort(key=lambda x: get_strength(x["hand"], joker=True))
        print()
        for (typ, hs) in hand_types.items():
            print("typ:", typ)
            for h in hs:
                print("-".join(h), end=" ")
            print()
        print()
        total_winnings_with_joker = 0
        for i in range(len(hands)):
            total_winnings_with_joker += hands[i]["bid"] * (i+1)



        for row in hands:
            strength = get_strength(row["hand"], joker=True)
            typ = row["typ"]
            if typ != "" and str(strength)[0] != typ:
                print(strength, row)
                exit()



        print(f"{file}: Total winnings = {total_winnings}")
        print(f"{file}: Total winnings with joker = {total_winnings_with_joker}")
        if file == files[0]:
            if total_winnings != 6440:
                print(f"Total winnings: {total_winnings} != 6440")
                break
            if total_winnings_with_joker != 5905:
                print(f"Total winnings with joker: {total_winnings_with_joker} != 5905")
                break
        else:
            if total_winnings_with_joker in [245658290, 245203400, 245246493]:
                print(f"Already guessed {total_winnings_with_joker}!")
                break
