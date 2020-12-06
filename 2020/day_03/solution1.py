def open_input(day):
    with open('./2020/day_{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        split_data = data.splitlines()
        return split_data

def count_tree_encounters(input):
	row_length = len(input[0])
	column_tracker = 0
	tree_count = 0

	for row in input:
		if column_tracker >= row_length:
			column_tracker = 0 + (column_tracker % row_length)
		path_spot = row[column_tracker]

		if (path_spot == '#'):
			tree_count += 1
		
		column_tracker += 3
	print(tree_count)

input = open_input("03")
count_tree_encounters(input)