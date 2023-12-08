import re

if __name__ == '__main__':
    files = ["input_data/day5_example1.txt", "input_data/day5.txt"]

    for file in files:
        with open(file, 'r') as f:
            data = f.readlines()

        sources = ["seed"]
        seeds = [int(x) for x in (data[0].removeprefix("seeds: ").strip().split(" "))]
        src_values = [[x] for x in seeds]
        src_values_seed_ranges = []
        for i in range(0, len(seeds), 2):
            start = seeds[i]
            length = seeds[i+1]
            src_values_seed_ranges.append([[start, start+length]])


        dest_values = []
        grouped_rows = []
        map_num = 0
        for row in data[2:len(data)]:
            if row == "\n":
                matches = re.match(r'([a-z]+)-to-([a-z]+) map:\n', grouped_rows[0])
                source = matches.group(1)
                destination = matches.group(2)
                sources.append(destination)
                for seed_num in range(len(src_values)):
                    isMapped = False
                    for ranges in grouped_rows[1:len(grouped_rows)]:
                        dest = int(ranges.split(" ")[0])
                        src = int(ranges.split(" ")[1])
                        length = int(ranges.split(" ")[2])
                        if src <= src_values[seed_num][map_num] < src + length:
                            v = src_values[seed_num][map_num] - src
                            d = dest - src
                            src_values[seed_num].append(src_values[seed_num][map_num] + (dest - src))
                            isMapped = True

                    if not isMapped:
                        src_values[seed_num].append(src_values[seed_num][map_num])

                isMapped = False
                for seed_num in range(len(src_values_seed_ranges)):
                    isMapped = False
                    for ranges in grouped_rows[1:len(grouped_rows)]:
                        dest = int(ranges.split(" ")[0])
                        src = int(ranges.split(" ")[1])
                        length = int(ranges.split(" ")[2])
                        if src <= src_values_seed_ranges[seed_num][map_num][0] and src_values_seed_ranges[seed_num][map_num][1] < src + length:
                            v = src_values_seed_ranges[seed_num][map_num][0] - src
                            d = dest - src
                            mappedSet = [src_values_seed_ranges[seed_num][map_num][0] + (dest - src), src_values_seed_ranges[seed_num][map_num][1] + (dest - src)]
                            src_values_seed_ranges[seed_num].append(mappedSet)
                            isMapped = True

                    if not isMapped:
                        src_values_seed_ranges[seed_num].append(src_values_seed_ranges[seed_num][map_num])

                grouped_rows = []
                map_num += 1
            else:
                grouped_rows.append(row)
            print()

        # for row in src_values:
        #     for i in range(len(row)):
        #         print(sources[i], row[i], end=", ")
        #     print()

        locations = [x[len(x) - 1] for x in src_values]
        locations_seed_range = [x[len(x)-1] for x in src_values_seed_ranges]
        min_location = min(locations)
        min_location_seed_ranges = min(locations_seed_range)

        foo = 0
        print(f"{file}: Min Location = {min_location}")
        print(f"{file}: Min Location Seed Ranges = {min_location_seed_ranges}")
        if file == files[0]:
            if min_location != 35:
                print(f"Min location: {min_location} != 35")
                break
            if min_location_seed_ranges != 46:
                print(f": {min_location_seed_ranges} != 46")
                break
