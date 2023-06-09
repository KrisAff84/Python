# Assertions are assumptions that should always be true

def calculate_inverse(number):
    assert (number != 0), 'Got 0 as number!'
    return 1 / number

print(calculate_inverse(0))  # If number is zero python will throw an AssertionError

# In general assertions are used for debugging and testing
# Not an error handling tool

