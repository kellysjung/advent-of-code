import re

def open_input(day):
    with open('./2020/day_{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        splitData = data.splitlines()
        return splitData

def validate_year(entry, lower, upper):
	entry = int(entry)
	if len(str(entry)) == 4 and entry >= lower and entry <= upper:
		return True
	return False

def validate_height(entry):
	if 'cm' in entry:
		value = int(entry.split('cm')[0])
		if value >= 150 and value <= 193:
			return True
	elif 'in' in entry:
		value = int(entry.split('in')[0]) 
		if value >= 59 and value <= 76:
			return True
	
	return False

def validate_hair_color(entry):
	if entry.startswith('#'):
		hex_match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', entry)
		if hex_match:
			return True
	return False

def validate_eye_color(entry):
	if len(entry) != 3:
		return False
	if entry == "amb" or entry == "blu" or entry == "brn" or entry == "gry" or entry == "grn" or entry == "hzl" or entry == "oth":
		return True
	return False

def validate_passport_id(entry):
	if re.search(r'^(\d{9})$', entry):
		return True
	return False

def is_passport_valid(credentials):
	credentials_check = [0, 0, 0, 0, 0, 0, 0, 0]
	credentials = ' '.join(credentials).split()
	
	for row in credentials:
		if row.startswith('byr:') and validate_year(row.split('byr:')[1], 1920, 2002):
			credentials_check[0] = 1
		elif row.startswith('iyr:') and validate_year(row.split('iyr:')[1], 2010, 2020):
			credentials_check[1] = 1
		elif row.startswith('eyr:') and validate_year(row.split('eyr:')[1], 2020, 2030):
			credentials_check[2] = 1
		elif row.startswith('hgt:') and validate_height(row.split('hgt:')[1]):
			credentials_check[3] = 1
		elif row.startswith('hcl:') and validate_hair_color(row.split('hcl:')[1]):
			credentials_check[4] = 1
		elif row.startswith('ecl:') and validate_eye_color(row.split('ecl:')[1]):
			credentials_check[5] = 1
		elif row.startswith('pid:') and validate_passport_id(row.split('pid:')[1]):
			credentials_check[6] = 1
		elif row.startswith('cid:'):
			credentials_check[7] = 1
	
	for field in credentials_check[:7]:
		if field == 0:
			return False

	return True

def count_valid_passports(input):
	credentials = []
	valid_passports_count = 0

	for row in input:
		if row:
			credentials.append(row)
		
		if (not row) or (row == input[len(input)-1]):
			if is_passport_valid(credentials):
				valid_passports_count += 1
			credentials = []

	return valid_passports_count



input = open_input("04")
print(count_valid_passports(input))