# Exercise for creating simple classes and instances of those classes

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name}.")
        print(f"{self.name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")


class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, username, email, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.age = age

    def describe_user(self):
        print(f"User's full name: {self.first_name} {self.last_name}")
        print(f"User's Age: {self.age}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! I hope you are having a great day!")


red_lobster = Restaurant('Red Lobster', 'seafood')
red_lobster.describe_restaurant()

mandolas = Restaurant('Mandolas', 'Italian food')
mandolas.describe_restaurant()

uchi = Restaurant('Uchi', 'sushi')
uchi.describe_restaurant()
uchi.open_restaurant()

user1 = User('Kris', 'Afflerbaugh', 'KrisAff84', 'krisaff@gmail.com', 'Austin, TX', 39)
user2 = User('Cara Ann', 'Afflerbaugh', 'CaraAnn85', 'caraannaff@gmail.com', 'Austin, TX', 38)

user1.describe_user()
user1.greet_user()
user2.describe_user()