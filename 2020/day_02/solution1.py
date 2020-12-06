import re

def open_input(day):
    with open('./2020/day_{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        split_data = data.splitlines()
        return split_data

def validate_passwords_1(inputs):
	valid_passwords_count = 0

	for input in inputs:
		split_input = re.search(r'(\d{1,2})-(\d{1,2})\s([a-z]):\s([a-z]*)', input).groups()
		lower_bound = int(split_input[0])
		upper_bound = int(split_input[1])
		char_checking = split_input[2]
		password_checking = split_input[3]
		count = 0

		for char in password_checking:
			if (char == char_checking):
				count += 1
		if (count >= lower_bound) and (count <= upper_bound):
			valid_passwords_count += 1
	print (valid_passwords_count)
			

inputs = open_input("02")
validate_passwords_1(inputs)