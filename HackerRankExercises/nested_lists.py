if __name__ == '__main__':
    grade_records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grade_records.append([name, score])
    
    # Sort the list of lists by the second element of each list
    grade_records.sort(key=lambda x: x[1])

    # Find the second lowest grade. If there are multiple students with the same grade, print all of them in alphabetical order.
    second_lowest_grade = sorted(set([grade for name, grade in grade_records]))[1]
    for name, grade in sorted(grade_records):
        if grade == second_lowest_grade:
            print(name)

        