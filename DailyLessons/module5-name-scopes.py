# Scope of variable name refers to part of the code where the name is recognized
# and can be used


def show_truth():
    print(mysterious_var)


mysterious_var = 'Surprise!'  # can define var outside of function and it still works

show_truth()

# Consider the following


def print_greeting():
    greeting = 'Hello Kris, I hope you are having a great day!'
    print(greeting)


# Shadowing: Python can see there is already a variable outside of the function
# For purpose of function a second temporary variable with the same is created
#
greeting = 'Good Morning!'  # Global variable
print(greeting)
print_greeting()      # Local variable is used
print(greeting)


# Can also define the use of global variables within function
# Example

def good_night():
    global night
    night = 'Good night Silas!'
    print(night)


night = 'Good night'
good_night()
print(night)
# After function is called the variable of night defined in function
# becomes the new global variable
# Rarely used in practice, as a general rule try to avoid using global
# Can also use .append for variables which will append global variable
