if __name__ == '__main__':
    s = input()
    list = [i for i in s]
    print(any([i.isalnum() for i in list]))
    print(any([i.isalpha() for i in list]))
    print(any([i.isdigit() for i in list]))
    print(any([i.islower() for i in list]))
    print(any([i.isupper() for i in list]))