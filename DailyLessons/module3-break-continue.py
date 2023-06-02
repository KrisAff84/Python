# break used to exit loop
while True:
    name = input('Enter your name or EXIT to close the program: ')
    if name == 'EXIT':
        break
    print('Hello', name)


# continue is used to exit current iteration and move on

# If we encounter a number that can be divided by 5,
# we don't exit whole loop.
for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)


