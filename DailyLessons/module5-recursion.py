# Recursion occurs when a function calls itself
# Factorials
# 3! = 1 * 2 * 3 = 6
# 5! = 1 * 2 * 3 * 4 * 5 = 120

def get_factorial(number):
    factorial = 1
    for x in range(1, number + 1):
        factorial *= x
    return factorial

# The above version of function is iterative
print(get_factorial(6))

# Now using recursion
# Facorial of 3 is 3 * 2!
# Factorial of 4 is 4 * 3! and so on ...

def get_factorial_recursive(number):
    if number <= 1:
        return 1
    return number * get_factorial_recursive(number - 1)


print(get_factorial_recursive(6))

# Recursion is worth knowing but most developers use it infrequently

