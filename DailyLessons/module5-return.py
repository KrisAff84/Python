def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average

# Don't use brackets around keyword return because it is not a function

print('The average is:', get_average([53.0, 32.6, 72.8, 9.9, 17.3]))

average = get_average([53.0, 32.6, 72.8, 9.9, 17.3])
if average > 32:
    print('The average is too high!')

# return gives result but also immediately exits function
# Any instruction after return (within function) will be ignored


def is_first_last_equal(number_list):
    if len(number_list) == 0:
        return
    if number_list[0] == number_list[-1]:
        return True
    else:
        return False


print(is_first_last_equal([10, 20, 30, 40, 10]))
print(is_first_last_equal([10, 20, 30, 40, 50]))
print(is_first_last_equal([]))
