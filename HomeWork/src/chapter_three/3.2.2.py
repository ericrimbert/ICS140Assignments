# 3.2.2: List functions and methods.

# part 1
user_ages = [9, 1, 4, 6, 7, 3]
list_length = len(user_ages)

# part 2
user_ages_pop = [99, 22, 77]
popped = user_ages.pop(0)


# part 3
user_ages_1 = [5, 6, 4, 2, 8, 3]
user_ages_2 = [1, 2, 44, 32, 23]
list_3 = user_ages_1 + user_ages_2

# part 4
user_ages_index = [9, 1, 4, 6, 7, 3]
index_9 = user_ages_index.index(9)

# part 5
user_ages_sum = [9, 1, 4, 6, 7, 3]
sum_user_ages = sum(user_ages_sum)

print(f"Part 1: {list_length}\nPart 2: {popped}\nPart 3: {list_3}\nPart 4: {index_9}\nPart 5: {sum_user_ages}")
