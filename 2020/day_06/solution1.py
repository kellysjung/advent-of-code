def open_input(day):
    with open('./2020/day_{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        split_data = data.splitlines()
        return split_data

def count_yeses(answers):
	yes_answers = ''
	group_answers = ''.join(set(answers))

	for char in group_answers:
		if char in yes_answers:
			pass
		else:
			yes_answers += char

	return len(yes_answers)

def count_total_answers(input):
	answers = []
	total_yes_count = 0

	for row in input:
		if row:
			answers.append(row)
		
		if (not row) or (row == input[len(input)-1]):
			total_yes_count += count_yeses(answers)
			answers = []
	return total_yes_count


input = open_input("06")
print(count_total_answers(input))