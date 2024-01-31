class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        # Attributes that change over time are called fields
        # Attributes that don't change over time are called constants
        self.make = make
        self.model = model
        self.year = year
        # Setting a default value for an attribute
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name
        
my_car = Car('Lexus', 'RX330', 2005)
print(my_car.get_descriptive_name())
print(my_car.odometer_reading)
    