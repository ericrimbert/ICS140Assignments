# 8.1.1: Modify a list.
#
short_names = ['Gertrude', 'Sam', 'Ann', 'Joseph']

short_names.pop(0)
short_names[len(short_names)-1] = 'Joe'

print(short_names)
# 8.2.1: Reverse sort of list.
#
short_names = ['Jan', 'Sam', 'Ann', 'Joe', 'Tod']

short_names.sort(reverse=True)

print(short_names)
# 8.3.1: Get user guesses.
#
num_guesses = 3
user_guesses = []

while len(user_guesses) < num_guesses:
    guess = int(input("Please enter in a guess: "))
    user_guesses.append(guess)

print(user_guesses)
# 8.3.2: Sum extra credit.
#
test_grades = [101, 83, 107, 90]
sum_extra = 0  # Initialize 0 before your loop
index = 0

while index < len(test_grades):
    extra_points = test_grades[index] - 100
    if extra_points > 0:
        sum_extra += extra_points
    index += 1


print('Sum extra:', sum_extra)
# 8.3.3: Hourly temperature reporting.
#
hourly_temperature = [90, 92, 94, 95]

index = 0
temps = ""

while index < len(hourly_temperature) -1:
    temps += str(hourly_temperature[index]) + " -> "
    index += 1

temps += str(hourly_temperature[len(hourly_temperature)-1]) + " "
print(f'{temps}')

# 8.5.1: Print multiplication table.
#
mult_table = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]

for nest in mult_table:
    string = ""
    for item in nest:
        string += str(item) + " | "
    print(string.rstrip(" | "))

# 8.12.1: Delete from dictionary.
#
country_capital = {'Spain': 'Madrid', 'Togo': 'Lome', 'Prussia': 'Konigsberg'}

if 'Prussia' in country_capital:
    country_capital.pop("Prussia")

print('Prussia deleted?', end=' ')
if 'Prussia' in country_capital:
    print('No.')
else:
    print('Yes.')
# 8.14.1: Report country population.
#
country_pop = {
    'China':         1365830000,
    'India':         1247220000,
    'United States': 318463000,
    'Indonesia':     252164800
}
# country populations as of 2014
for country, population in country_pop.items():
    print(country, 'has', pop, 'people.')

