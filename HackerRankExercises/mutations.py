def mutate_string(string, position, character):
    # [:position] takes the string from one character before the value of position
    # [position+1:] takes the string from one character after the value of position
    return string[:position] + character + string[position+1:]
    
    # This longer way accomplishes the same thing
    # list(string)[position] = character
    # string_list = list(string)
    # string_list[position] = character
    # return ''.join(string_list)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)