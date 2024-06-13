# Determines whether input is leap year or not, True or False

def is_leap(year):
    leap = False
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
    
    print(leap)
    return leap

def main():
    year = int(input('Enter year: '))
    is_leap(year)

if __name__ == "__main__":
    main()










