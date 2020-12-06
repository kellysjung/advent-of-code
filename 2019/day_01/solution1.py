import math

def open_input(day):
    with open('./2019/day_{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        split_data = data.splitlines()
        return split_data

def calculate_total_fuel_requirement(input):
	total_fuel = 0

	for mass in input:
		fuel = math.floor(int(mass) / 3) - 2
		total_fuel += fuel

	return total_fuel

input = open_input("01")
print(calculate_total_fuel_requirement(input))