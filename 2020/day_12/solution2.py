def open_input(day):
    with open('./2020/day_{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        split_data = data.splitlines()
        return split_data

def turn_right(direction, degrees):
	turns = degrees / 90
	if direction + turns > 4:
		direction = int((direction + turns) % 4)
	else:
		direction += turns
	return direction

def turn_left(direction, degrees):
	turns = degrees / 90
	if direction - turns <= 0:
		direction = int(direction - turns + 4)
	else:
		direction -= turns
	return direction

def find_manhattan_distance_from_waypoint(instructions):
	# North = 1, East = 2, South = 3, West = 4
	direction = 2
	x = y = 0
	for move in instructions:
		letter = move[0]
		number = int(move[1:])

		if letter == 'R' or letter == 'L':
			if letter == 'R':
				direction = turn_right(direction, number)
			elif letter == 'L':
				direction = turn_left(direction, number)
		elif letter == 'F':
			
		else:
			if letter == 'E':
				waypoint_direction = turn_right(direction, 90)
			elif letter == 'S':
				waypoint_direction = turn_right(direction, 180)
			elif letter == 'W':
				waypoint_direction = turn_right(direction, 270)
			else:
				waypoint_direction = direction

			if waypoint_direction == 1:
				y += number
			elif waypoint_direction == 3:
				y -= number
			elif waypoint_direction == 2:
				x += number
			elif waypoint_direction == 4:
				x -= number
			else:
				return -1
	return abs(x) + abs(y)

input = open_input("12")
print(find_manhattan_distance_from_waypoint(input))