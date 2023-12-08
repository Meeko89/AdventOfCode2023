
if __name__ == '__main__':
    files = ["input_data/day5_example1.txt", "input_data/day5.txt"]

    for file in files:
        with open(file, 'r') as f:
            data = f.readlines()




        foo = 0
        print(f"{file}: A = {foo}")
        print(f"{file}: B = {foo}")
        if file == files[0]:
            if foo != 0:
                print(f": {foo} != 0")
                break
            if foo != 0:
                print(f": {foo} != 0")
                break
