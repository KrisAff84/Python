# for long lists
# could use, but takes up more space
numbers = []
for i in range(1, 101):
    numbers.append(i)
print(numbers)

# Use list comprehension instead
numbers = [i for i in range(1, 101)]
print(numbers)

# Same thing but skip numbers divisible by 3
numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)
