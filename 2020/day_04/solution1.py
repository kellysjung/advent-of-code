import re

def open_input(day):
    with open('./2020/day_{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        splitData = data.splitlines()
        return splitData

def is_passport_valid(credentials):
	credentials_check = [0, 0, 0, 0, 0, 0, 0, 0]
	for row in credentials:

		if (row.find('byr:') != -1):
			credentials_check[0] = 1
		if (row.find('iyr:') != -1):
			credentials_check[1] = 1
		if (row.find('eyr:') != -1):
			credentials_check[2] = 1
		if (row.find('hgt:') != -1):
			credentials_check[3] = 1
		if (row.find('hcl:') != -1):
			credentials_check[4] = 1
		if (row.find('ecl:') != -1):
			credentials_check[5] = 1
		if (row.find('pid:') != -1):
			credentials_check[6] = 1
		if (row.find('cid:') != -1):
			credentials_check[7] = 1
	
	for field in credentials_check[:7]:
		if field == 0:
			return False

	return True


def count_valid_passports(input):
	credentials = []
	credentials_count = 0
	valid_passports_count = 0

	for row in input:
		if row:
			credentials.append(row)
		
		if (not row) or (row == input[len(input)-1]):
			if is_passport_valid(credentials):
				valid_passports_count += 1
			credentials = []
			credentials_count += 1

	return valid_passports_count


input = open_input("04")
print(count_valid_passports(input))