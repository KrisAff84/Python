if __name__ == '__main__':
    number_of_students = int(input('Enter number of students: '))
    student_marks = {}
    print('Enter student name, followed by individual scores, one student per line. Separate values with spaces:')
    for _ in range(number_of_students):
        name, *marks = input().split()
        scores = list(map(float, marks))
        student_marks[name] = scores
    print(f'Students: {", ".join(student_marks.keys())}')
    print('Enter a student name to calculate their score average:')
    query_name = input()
    # Calculate the average scores of the student in the query_name
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    # Format the average to two decimal places
    print(f'{average:.2f}')