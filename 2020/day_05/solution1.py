def open_input(day):
    with open('./2020/day_{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        split_data = data.splitlines()
        return split_data

input = open_input("05")