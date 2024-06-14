numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square_of_evens = [pow(n, 2) for n in numbers if n % 2 == 0]
print(square_of_evens)