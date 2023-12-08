import re

if __name__ == '__main__':
    files = ["input_data/day4_example1.txt", "input_data/day4.txt"]

    for file in files:
        with open(file, 'r') as f:
            data = f.readlines()

        points = {}
        won_scratchpads = {}

        for ticket in data:
            matched_count = 0
            ticket_match = re.match(r'Card +([0-9]+):([0-9 ]+)\|([0-9 ]+)', ticket)
            ticket_id = int(ticket_match.group(1))
            winning_numbers = {s: True for s in ticket_match.group(2).strip().split(" ") if len(s) > 0}
            ticket_numbers = [s for s in ticket_match.group(3).strip().split(" ") if len(s) > 0]

            for number in ticket_numbers:
                if number in winning_numbers:
                    matched_count += 1

            if matched_count:
                points[ticket_id] = (pow(2, matched_count-1))
            else:
                points[ticket_id] = 0

            for i in range(1, matched_count+1):
                if ticket_id in won_scratchpads:
                    copies = won_scratchpads[ticket_id] + 1
                else:
                    copies = 1
                if ticket_id+i in won_scratchpads:
                    won_scratchpads[ticket_id + i] += copies
                else:
                    won_scratchpads[ticket_id + i] = copies
            # print(ticket_id, ": ", matched_count, " -> ", points[ticket_id])

        total_points = sum(points.values())
        nb_scratchpads = sum(won_scratchpads.values()) + len(data)
        print(f"{file}: winning points = {total_points}")
        print(f"{file}: number of scratchpads: {nb_scratchpads}")
        if file == files[0]:
            if total_points != 13:
                print(f"Total points: {total_points} != 13")
                break
            if nb_scratchpads != 30:
                print(f"Number of scratchpads: {nb_scratchpads} != 30")
                break
