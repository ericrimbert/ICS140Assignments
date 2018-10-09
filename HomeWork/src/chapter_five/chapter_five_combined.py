# 5.2.1: Basic while loop with user input.
#
user_num = 9
while user_num >= 0:
    print('Body')
    user_num = int(input())

print('Done.')
# 5.2.2: Basic while loop expression.
#
user_num = 20

while user_num >= 1:
    user_num /= 2
    print(user_num)
# 5.3.1: Bidding example.
#
import random
random.seed(5)

keep_going = '-'
next_bid = 0

while keep_going != 'n':
    next_bid = next_bid + random.randint(1, 10)
    print('I\'ll bid $%d!' % (next_bid))
    print('Continue bidding?', end=' ')
    keep_going = input()
# 5.3.2: While loop: Insect growth.
#
num_insects = 8  # Must be >= 1
num_string = str(num_insects)
while 1 <= num_insects <= 100:
    num_insects *= 2
    if num_insects <= 100:
        num_string += f" {num_insects}"

print(num_string)
# 5.4.1: While loop: Print 1 to N.
#
i = 1
user_num = 4  # Assume positive
print(i)
while i < user_num:
    i += 1
    print(i)

# 5.4.2: Printing output using a counter.
#
num_stars = 3
num_printed = 0

while num_printed != num_stars:
    print('*')
    num_printed += 1

# 5.5.1: For loop: Printing a list
# Apple (APPL) stock prices 2005-2007
stock_prices = [34.62, 76.30, 85.05]
for price in stock_prices:
    print('$', price)

# 5.5.2: For loop: Printing a dictionary
#
contact_emails = {
    'Sue Reyn': 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}

for key, value in contact_emails.items():
    print(f"{value} is {key}")

# 5.8.1: Nested loops: Print rectangle
#
num_rows = 6
num_cols = 6
i = 0
x = 1
star_string = '*'
while i < num_rows:
    while x < num_cols:
        star_string += ' *'
        x += 1
    print(star_string)
    i += 1

# 5.10.1: Simon says.
#
user_score = 0
simon_pattern = 'RRGBRYYBGY'
user_pattern = 'RRGBBRYBGY'
i = 0
for char in user_pattern:
    if char == simon_pattern[user_score]:
        user_score += 1
    else:
        break
print('User score:', user_score)
