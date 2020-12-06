def open_input(day):
    with open('./2020/day_{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        split_data = data.splitlines()
        return split_data

def count_tree_encounters(input, right, down):
	row_length = len(input[0])
	column_tracker = 0
	tree_count = 0
	row_tracker = 0

	while (row_tracker < len(input)):
		row = input[row_tracker]
		if column_tracker >= row_length:
			column_tracker = 0 + (column_tracker % row_length)
		path_spot = row[column_tracker]

		if (path_spot == '#'):
			tree_count += 1
		
		column_tracker += right
		row_tracker += down
	return(tree_count)

input = open_input("03")
a = (count_tree_encounters(input, 1, 1))
b = (count_tree_encounters(input, 3, 1))
c = (count_tree_encounters(input, 5, 1))
d = (count_tree_encounters(input, 7, 1))
e = (count_tree_encounters(input, 1, 2))

print (a*b*c*d*e)