# # lab 3
#
# Part 1: Understanding of basic string operations.
# -------------------------------------------------

# Ask the user to enter a string.
user_input = input("Please enter in a string: ")

# Print out the first character of the string, the last character of the string and the length of the string.
print(f"First Character: {user_input[0]}, Last Character: {user_input[-1]}, Length of the string: {len(user_input)}.")
#
# Print out the position in which a Z exists in the string.
print(f"Index of the letter Z: {user_input.find('Z')}")
#
# Print out the string with the first character duplicated.
print(f"{user_input[0] + user_input}")

# Part 2: Understanding of basic list operations.
# ------------------------------------------------
#
# Create a list consisting of the strings: ABC, GHI, JKL.
string_list = ['ABC', 'GHI', 'JKL']
print(string_list)
#
# Append MNO to the list.
string_list.append('MNO')
print(string_list)
#
# Change the second element in the list to PQR.
string_list[1] = 'PQR'
print(string_list)
#
# Remove the element ABC from the list.
string_list.remove('ABC')
print(string_list)
#
# Part 3: Understanding of basic dictionary operations.
# -----------------------------------------------------
#
# Create a dictionary consisting of the keys and values:
#
# Key   | Value
# -----------------
# 55118 | Saint Paul
# 40218 | Louisville
# 90210 | Beverly Hills
loc_dict = {'55118': 'Saint Paul', '40218': 'Louisville', '90210': 'Beverly Hills'}
print(loc_dict)

# add and remove values.
loc_dict['55101'] = 'Minneapolis'
loc_dict.pop('40218')
print(loc_dict)
