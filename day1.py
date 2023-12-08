import re


def solve(data: list[str]) -> int:

    coords = []
    for row in data:
        match = re.findall(r'[0-9]', row)
        coords.append(int(match[0] + match[len(match)-1]))

    return sum(coords)


def get_number(s: str) -> str:
    ans = 0
    numbers = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }
    if len(s) > 1:
        return numbers[s]

    return s


def solve2(data: list[str]) -> int:

    coords = []
    for row in data:
        match = re.findall(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', row)
        x = get_number(match[0])
        y = get_number(match[len(match)-1])
        z = int(x+y)
        coords.append(z)

    return sum(coords)


if __name__ == '__main__':

    with open("./input_data/day1_exemple.txt", 'r') as f:
        data = f.readlines()

    print("Example 1: ", solve(data))

    with open("./input_data/day1.txt", 'r') as f:
        data = f.readlines()

    print("Answer: ", solve(data))

    with open("./input_data/day1_example2.txt", 'r') as f:
        data = f.readlines()

    print("Example 2: ", solve2(data))

    with open("./input_data/day1.txt", 'r') as f:
        data = f.readlines()

    print("Answer: ", solve2(data))
