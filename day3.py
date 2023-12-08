def symbol_adjacent(data, coords, num, row, start, end):
    loops = 0
    mapped = []
    for r in range(row-1, row+2):
        line = []
        if r < 0 or r >= len(data):
            continue
        for c in range(start-1, end+2):
            if c < 0 or c >= len(data[r]):
                continue
            if data[r][c] == ".":
                line.append(" ")
            else:
                line.append(data[r][c])
        mapped.append(line)
        # print(line)
    loops = 0

    for (r, c) in coords:
        for x in range(-1, 2):
            for y in range(-1, 2):
                # print(x, ",", y)
                loops += 1
                if r+x < 0 or c+y < 0 or r+x >= len(data) or c+y >= len(data[x]):
                    continue
                d = data[r][c]
                ch = data[r+x][c+y]
                if data[r+x][c+y] not in "0123456789.\n":
                    # print(True)
                    return [r+x, c+y]
    # print(False)
    return None


if __name__ == '__main__':

    files = ["input_data/day3_example1.txt", "input_data/day3.txt"]

    for file in files:
        with open(file, 'r') as f:
            data = f.readlines()
        summed_parts = 0
        gear_ratio = 0
        star_parts = {}
        nums = []
        for r in range(len(data)):
            coords = []
            start = -1
            end = -1
            num = ""
            for c in range(len(data[r])):
                ch = data[r][c]
                if ch.isnumeric():
                    if not num:
                        start = c
                    end = c
                    coords.append((r, c))
                    num += ch
                elif coords:
                    symbol_pos = symbol_adjacent(data, coords, num, r, start, end)
                    if symbol_pos is not None:
                        summed_parts += int(num)
                        nums.append(int(num))
                        # print(num)
                        symbol = data[symbol_pos[0]][symbol_pos[1]]
                        if symbol == '*':
                            star_pos = ",".join([str(i) for i in symbol_pos])
                            if star_pos in star_parts:
                                star_parts[star_pos].append(int(num))
                            else:
                                star_parts[star_pos] = [int(num)]

                    num = ""
                    coords = []

        for gears in star_parts.values():
            if len(gears) == 2:
                gear_ratio += gears[0] * gears[1]

        print(file, ": SUM = ", summed_parts)
        print(file, ": gear_ratios = ", gear_ratio)
        if file == files[0]:
            if summed_parts != 4361:
                print(f"SUM: {summed_parts} != 4361")
                break
            if 467835 != gear_ratio:
                print(f"Gear Ratios: {gear_ratio} != 467835")
                break






