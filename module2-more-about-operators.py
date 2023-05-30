# Binary operators

print(5 + 7)
print(5 - 7)

# Unary operators

print(+12)
print(-2)


# Order of operators
# 1.) ()
# 2.) **
# 3.) * / // %
# 4.) + -

print(2 + 3 * 2)   #Python multiplies 3 * 2 first
print((2 + 3) * 2)  # Python adds 2 + 3 first

# floats are not represented exactly in binary, as an example

print(0.1 + 0.1 + 0.1)  # Should be 0.3

# Power operators- Python starts on right with multiple power operators
# Right-sided binding
# All other operators are left-sided bound

print(2 ** 2 ** 3)  # = (2 ** 3) = 8, 2 ** 8 = 256
# not (2 ** 2) = 4, 4 ** 3 = 64

print((2 ** 2) ** 3)  # use parenthesis to change order of powers



