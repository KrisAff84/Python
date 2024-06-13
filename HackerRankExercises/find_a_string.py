def count_substring(string, sub_string):
    ''' 
    Iterates through string and checks if sub_string is in string, counting the number of times
    The main statement returns True (if the sub_string is found in the string, starting at 
    index i). The len function counts the number of times the statement is True.
    If the first len function is removed, the function will return a list of indexes where
    the sub string is found in the string.
    '''
    return len([i for i in range(len(string)) if string.startswith(sub_string, i)])

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)