import re

def open_input(day):
    with open('./2020/day_{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        split_data = data.splitlines()
        return split_data

def validate_passwords_2(inputs):	
	valid_passwords_count = 0

	for input in inputs:
		split_input = re.search(r'(\d{1,2})-(\d{1,2})\s([a-z]):\s([a-z]*)', input).groups()
		first_position = int(split_input[0])
		second_position = int(split_input[1])
		char_checking = split_input[2]
		password_checking = split_input[3]

		if (password_checking[first_position-1] == char_checking) ^ (password_checking[second_position-1] == char_checking):
			valid_passwords_count += 1

	print (valid_passwords_count)
			

inputs = open_input("02")
validate_passwords_2(inputs)