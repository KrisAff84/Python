#!/bin/python3

"""
Takes input from a string, splits, and capitalizes each word in the string.
"""
def solve(s):
    split_string = s.split(' ')
    return ' '.join([word.capitalize() for word in split_string])
    

if __name__ == '__main__':
    
    s = input()

    result = solve(s)

    print(result)


