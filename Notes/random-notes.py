import random
import string



# generates random float between 0 and 1
value = random.random()
print(value)

# generates random float between two numbers
value = random.uniform(1, 10)
print(value)

# generates random int between two numbers
value = random.randint(1, 6)
print(value)

# picks random value from list of values
greetings = ['Hello', 'Hi', 'Wazzup', 'Howdy', 'Hola', 'Good day', 'Top of the \'mornin']

value = random.choice(greetings)
print(value + ', Kris')

# picks multiple choices, k is how many times to run
colors = ['Red', 'Black', 'Green']

results = random.choices(colors, k=10)
print(results)

# to weight choices
results = random.choices(colors, weights=[18, 18, 2], k=10)
print(results)

# randomly shuffle list of values
deck = list(range(1, 53))  # top number is non-inclusive

random.shuffle(deck)
print(deck)

# select random sample from list
deck = list(range(1, 53))  # top number is non-inclusive

hand = random.sample(deck, k=5)
print(hand)

# for random letters
letters = ''.join(random.choices(string.ascii_letters, k=10))
print(letters)


# joining random letters with other variable
department = "Dev"
letters = ''.join(random.choices(string.ascii_letters, k=10))
print(letters + '-' + department)

characters = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
print(department + '-' + characters)

