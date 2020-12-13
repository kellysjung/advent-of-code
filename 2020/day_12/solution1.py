def open_input(day):
    with open('./2020/day_{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        split_data = data.splitlines()
        return split_data

def find_manhattan_distance(instructions):
	# North = 1, East = 2, South = 3, West = 4
	direction = 2
	x = y = 0
	for move in instructions:
		letter = move[0]
		number = int(move[1:])

		if letter == 'N':
			y += number
		elif letter == 'S':
			y -= number
		elif letter == 'E':
			x += number
		elif letter == 'W':
			x -= number
		elif letter == 'R':
			turns = number / 90
			if direction + turns > 4:
				direction = int((direction + turns) % 4)
			else:
				direction += turns
		elif letter == 'L':
			turns = number / 90
			if direction - turns <= 0:
				direction = int(direction - turns + 4)
			else:
				direction -= turns
		elif letter == 'F':
			if direction == 1:
				y += number
			elif direction == 3:
				y -= number
			elif direction == 2:
				x += number
			elif direction == 4:
				x -= number
		else:
			return -1
	return abs(x) + abs(y)
				

input = open_input("12")
print(find_manhattan_distance(input))