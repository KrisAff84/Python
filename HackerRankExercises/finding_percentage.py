if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    print(student_marks.keys())
    query_name = input()
    # Calculate the average scores of the student in the query_name
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    # Format the average to two decimal places
    print(f'{average:.2f}')