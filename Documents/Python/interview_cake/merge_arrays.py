def merge_lists(first_list, second_list):
	merged_list_length = len(first_list) + len(second_list)
	merged_list = [None] * merged_list_length
	i = 0
	j = 0
	k = 0

	while (k < merged_list_length):
		end_of_first_list = i >= len(first_list)
		end_of_second_list = j >= len(second_list)

		if (not end_of_first_list and (end_of_second_list or first_list[i] < second_list[j])):
			merged_list[k] = first_list[i]
			i += 1
		else:
			merged_list[k] = second_list[j]
			j += 1

		k += 1

	return merged_list


first_list = [3, 4, 6, 10, 11, 15]
second_list = [1, 5, 8, 12, 14, 19]

merged = merge_lists(first_list, second_list)
print(merged)