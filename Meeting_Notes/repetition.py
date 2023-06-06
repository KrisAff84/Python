import random
number = 0
while number < 10:
    print(number)
    number += 1
print()

number = 0
counter = 0
while number != 52:
    number = random.randint(0, 100)
    counter += 1
print(counter, number)

print()

for i in range(10):
    print(i * 2)

number = random.randint(0, 100)

# If you don't know how many times you need to do something, do it with a while loop
# If you do know, do it with a for loop
