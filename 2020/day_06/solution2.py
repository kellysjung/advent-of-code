def open_input(day):
    with open('./2020/day_{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        split_data = data.splitlines()
        return split_data

def count_yeses(group_answers):
	first_response = sorted(set(group_answers[0]))
	answer_counts = []
	
	if len(group_answers) == 1:
		return len(group_answers[0])

	for individual_answers in group_answers:
		answer_count = 0
		for answer in individual_answers:
			if answer in first_response:
				answer_count += 1
		answer_counts.append(answer_count)
	return sorted(answer_counts)[0]

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