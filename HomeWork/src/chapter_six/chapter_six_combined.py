# 6.1.1: Basic function call output.
#


def print_pattern():
    print('*****')
    return


i = 0
while i < 2:
    print_pattern()
    i += 1
# 6.1.2: Basic function call.
#


def print_shape():
    shape = '***\n***\n***'
    print(shape)
    return


print_shape()
# 6.2.1: Function call with parameter: Converting measurements.
#


def print_total_inches(num_feet, num_inches):
    num_inches = (num_feet*12) + num_inches
    print(f"Total inches: {num_inches}")
    return


print_total_inches(5, 8)
# 6.2.2: Function call with parameter: Print tic-tac-toe board.
#


def print_tic_tac_toe(horiz_char, vert_char):
    line_one = f"x {vert_char} x {vert_char} x"
    line_two = (f"{horiz_char} "*5).strip()
    i = 0
    while i < 2:
        print(f"{line_one}\n{line_two}")
        i += 1
    print(line_one)
    return


print_tic_tac_toe('~', '!')
# 6.3.1: Function call in expression.
#


def find_max(num_1, num_2):
    max_val = 0.0

    if num_1 > num_2:  # if num1 is greater than num2,
        max_val = num_1   # then num1 is the maxVal.
    else:                # Otherwise,
        max_val = num_2   # num2 is the maxVal
    return max_val


num_a = 5.0
num_b = 10.0
num_y = 3.0
num_z = 7.0

max_sum = find_max(num_a, num_b) + find_max(num_y, num_z)
print('max_sum is:', max_sum)
# 6.3.2: Function definition: Volume of a pyramid.
#


def pyramid_volume(base_length, base_width, pyramid_height):
    base_area = base_length * base_width
    volume = base_area * pyramid_height * (1/3)
    return volume


print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(4.5, 2.1, 3.0))
# 6.6.1: Function with branch: Popcorn.
#


def print_popcorn_time(bag_ounces):
    if bag_ounces < 3:
        print("Too small")
    elif bag_ounces > 10:
        print("Too large")
    else:
        print(f"{bag_ounces*6} seconds")
    return


print_popcorn_time(7)
# 6.6.2: Function with loop: Shampoo.
#


def shampoo_instructions(num_cycles):
    if num_cycles < 1:
        print("Too few.")
    elif num_cycles > 4:
        print("Too many.")
    else:
        n = 1
        while n <= num_cycles:
            print(f"{n} : Lather and rinse.")
            n += 1
        print("Done.")


shampoo_instructions(2)
# 6.7.1: Function stubs: Statistics.
#


def get_user_num():
    print('FIXME: Finish get_user_num()')
    return -1


def compute_avg(user_num1, user_num2):
    print('FIXME: Finish compute_avg()')
    return -1


user_num1 = get_user_num()
user_num2 = get_user_num()
avg_result = compute_avg(user_num1, user_num2)

print('Avg:', avg_result)
# 6.9.1: Function errors: Copying.
#


def celsius_to_kelvin(value_celsius):
    value_kelvin = value_celsius + 273.15
    return value_kelvin


def kelvin_to_celsius(value_kelvin):
    value_celsius = value_kelvin - 273.15
    return value_celsius


value_c = 10.0
print(value_c, 'C is', kelvin_to_celsius(value_c), 'K')

value_k = 283.15
print(value_k, 'is', kelvin_to_celsius(value_k), 'C')
# 6.13.1: Return number of pennies in total.
#


def number_of_pennies(dollars=0, pennies=0):
    total_pennies = (dollars*100) + pennies
    return total_pennies


print(number_of_pennies(5, 6))  # Should print 506
print(number_of_pennies(4))   # Should print 400
# 6.17.1: Function to compute gas volume.
#


gas_const = 8.3144621


def compute_gas_volume(pressure, temperature, moles):
    gas = moles * gas_const * temperature
    volume = gas / pressure
    return volume


gas_pressure = 100.0
gas_moles = 1.0
gas_temperature = 273.0

gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
print('Gas volume:', gas_volume, 'm^3')
