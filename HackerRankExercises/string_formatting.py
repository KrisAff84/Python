"""
Given integer n, print the following values for each integer i from
1 to n.

1. Decimal
2. Octal
3. Hex
4. Binary

Print to single line, space padded to match width of binary value of n,
and values separated by a single space. Align rightmost digits in each column.
"""

def print_formatted(number):
    s = len(str(bin(number)).lstrip('0b'))
    for i in range(1, number + 1):
        fl = f'{float(i):.0f}'
        o = str(oct(i)).lstrip('0o')
        h = str.upper(hex(i)).lstrip('0X')
        b = str(bin(i)).lstrip('0b')
        print(f'{fl.rjust(s)} {o.rjust(s)} {h.rjust(s)} {b.rjust(s)}')



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)