def calculate_jolt_differences(input):
    input.sort()
    i = 0
    one_count = 1
    three_count = 1

    while i < len(input) - 1:
        difference = input[i+1] - input[i]
        if difference == 1:
            one_count += 1
        elif difference == 3:
            three_count += 1
        else:
            return -1
        i += 1
    
    return one_count * three_count

def count_distinct_arrangements(input):
    input.sort()
    arrangements_count = 1
    i = 0

    while i < len(input) - 1:
        j = 1
        exceeded = False
        differences = []

        while not exceeded and j + i < len(input):
            difference = input[j+i] - input[i]
            differences.append(difference)
            if difference > 3:
                if len(differences) > 1:
                    print(differences)
                    arrangements_count += len(differences) - 1
                exceeded = True
            j += 1

        i += 1

    return arrangements_count
   
        

small_sample = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
large_sample = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
input = [77, 58, 25, 92, 14, 154, 105, 112, 147, 63, 84, 109, 24, 129, 49, 102, 130, 128, 134, 88, 95, 70, 80, 4, 153, 17, 145, 122, 39, 117, 93, 65, 3, 2, 139, 101, 148, 37, 27, 1, 87, 64, 23, 59, 42, 146, 43, 151, 116, 46, 115, 118, 131, 94, 19, 33, 12, 107, 10, 7, 73, 78, 53, 11, 135, 79, 60, 32, 141, 31, 140, 98, 136, 72, 38, 152, 30, 74, 106, 50, 13, 26, 155, 67, 20, 66, 91, 56, 34, 125, 52, 51, 18, 108, 57, 81, 119, 71, 144]
print(count_distinct_arrangements(small_sample))