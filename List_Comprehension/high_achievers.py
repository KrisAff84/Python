students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 72},
    {'name': 'Charlie', 'grade': 90},
    {'name': 'Dave', 'grade': 65},
    {'name': 'Eve', 'grade': 78}
]
# Your list comprehension here
high_achievers = [s['name'] for s in students if s['grade'] > 75]

