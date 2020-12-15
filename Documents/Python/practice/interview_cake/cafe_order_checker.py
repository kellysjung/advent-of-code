def is_first_come_first_served(take_out_list, dine_in_list, served_list):
	take_out_index = 0
	dine_in_index = 0
	served_list_index = 0

	while served_list_index < len(served_list):
		order = served_list[served_list_index]
		if (take_out_index < len(take_out_list)) and (order == take_out_list[take_out_index]):
			take_out_index += 1
		elif (dine_in_index < len(dine_in_list)) and (order == dine_in_list[dine_in_index]):
			dine_in_index += 1
		else:
			return False
		served_list_index += 1


	return True

print(is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6]))
print(is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5]))
print(is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8]))
