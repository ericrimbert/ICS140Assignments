# 2.7.1 - Compute change

# variables that sets amount, gets amount of 5s, and 1s
amount_to_change = 19
num_fives = amount_to_change // 5
num_ones = amount_to_change % (num_fives * 5)

# prints the total amount of 1s and 5s
print(f"Total amount of fives: {num_fives}, total amount of ones: {num_ones}.")