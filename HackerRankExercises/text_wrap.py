"""
Wrap string by maximum width 
"""

import textwrap

def wrap(string, max_width):
    """ Using the textwrap function alone produces a list, with each item
        of the list being max_width characters long. The join method is used
        with a newline (\n) character delimiter to print each item of the list 
        to a separate line.
    """
    return "\n".join(textwrap.wrap(string, width=max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)