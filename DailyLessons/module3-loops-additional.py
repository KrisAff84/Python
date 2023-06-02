for i in range(11):
    pass # doesn't do anything

# Why use?: loop requires at least 1 instruction inside
# of loop's body.

# Use case: might be in the middle of writing code and don't know what
# needs to be inside of loop's body yet. Use pass so that errors are
# not generated.

#### Nested Loops ######
for a in range(1, 11):
    for b in range(1, 11):  # Goes through all inner loop iterations first
        print(a, 'x', b, '=', a * b)

print()
print()
### Loops with else statements - rarely used in practice
## Else statement of loop is always executed exactly once
## Exception is with a break statement

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print('else:', i)

