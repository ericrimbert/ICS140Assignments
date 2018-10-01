# 4.2.1: Enter the output for the if-else branches.
#
num_apples = 4

if num_apples < 8:
   print('c')
else:
   print('d')

print('k')
# c
# k

numCats = 5

if numCats > 7:
    print('b')
else:
    print('e')

print('k')
# e
# k

num_apples = 7

if num_apples < 7:
    print('b')
else:
    print('e')

print('k')
# e
# k

# 4.2.2: Basic if-else expression.
#
user_age = 17
if user_age < 18:
   print('18 or less')
else:
   print('Over 18')

# 4.2.3: Basic if-else.
#
user_tickets = 0

if user_tickets < 5:
    num_tickets = 1
else:
    num_tickets = user_tickets

# 4.2.4: Multi-branch if-else statements: Print century.
#
year = 1776

if year >= 2101:
    print('Distant Future')
elif year >= 2001:
    print('21st Century')
elif year >= 1901:
    print('20th Century')
else:
    print('Long ago')

# 4.3.1: Enter the output for the multiple if-else branches.
#
num_items = 4

if num_items < 1:
    print('c')
elif num_items < 9:
    print('d')
else:
    print('g')

print('r')
# d
# r


num_sandwiches = 6

if num_sandwiches < 1:
    print('b')
elif num_sandwiches > 8:
    print('d')
else:
    print('k')

print('m')
# k
# m

num_puppies = 5

if num_puppies < 3:
    print('a')

if num_puppies > 8:
    print('f')

if num_puppies < 8:
    print('h')

print('r')
# h
# r


num_items = 6

if num_items > 3:
    print('a')

if num_items < 7:
    print('d')

if num_items == 6:
    print('g')

print('r')
# a
# d
# g
# r

# 4.3.2: Multiple if statements: Printing car features.
#
car_year = 1964

if car_year <= 1969:
    print("Few safety features.")
if car_year >= 1970:
    print("Probably has seat belts.")
if car_year >= 1990:
    print("Probably has anti-lock brakes.")
if car_year >= 2000:
    print("Probably has air bags.")

# 4.4.1: Enter the output for the branches with relational and equality operators.
#
num_eggs = 4

if num_eggs <= 5:
    print('a')
else:
    print('f')

print('h')
# a
# h


num_bikes = 5

if num_bikes >= 6:
    print('c')
else:
    print('f')

print('g')
# f
# g


num_puppies = 5

if num_puppies == 4:
    print('b')
else:
    print('f')

print('g')
# f
# g


num_apples = 6

if num_apples != 5:
    print('c')
else:
    print('e')

print('h')
# c
# h

# 4.4.2: Relational operators.
#
num_cents = 109
if num_cents >= 100:
    print('Dollar or more')
else:
    print('not a dollar')

# 4.4.3: If-else expression: Operator chaining.
#
user_grade = 10
if 9 <= user_grade <= 12:
    print('in high school')
else:
    print('not in high school')

# 4.5.1: Boolean operators: Detect specific values.
#
special_num = 17

if special_num == -99 or special_num == 0 or special_num == 44:
    print('Special number')
else:
    print('Not special number')

# 4.5.2: Boolean operators: Combining test conditions.
#
user_age = 17

if user_age > 17 and user_age != 25:
    print('Eligible')
else:
    print('Ineligible')

# 4.5.3: Boolean operators: Branching using Boolean variables.
#
young = True
famous = False

if young and famous:
    print('You must be rich!')
else:
    print('There is always the lottery...')

# 4.6.1: Boolean operators: Detect specific values.
#
special_list = [-99, 0, 44]
special_num = 17

if special_num in special_list:
    print('Special number')
else:
    print('Not special number')

# 4.8.1: Indentation: Fix the program.
#
temperatures = {
    'Seattle': 56.5,
    'New York': 105,
    'Kansas City': 81.9,
    'Los Angeles': 76.5
}

if 'New York' in temperatures:
    if temperatures['New York'] > 90:
        print('The city is melting!')
    else:
        print('The temperature in New York is', temperatures['New York'])
else:
    print('The temperature in New York is unknown.')

# 4.9.1: Conditional expression: Print negative or non-negative.
#
user_val = 0

if user_val < 0:
    cond_str = "negative"
else:
    cond_str = "non-negative"

print(user_val, 'is', cond_str)

# 4.9.2: Conditional expression: Conditional assignment.
num_users = 8
update_direction = 0

if update_direction == 3:
    num_users += 1
else:
    num_users -= 1

print('New value is:', num_users)

