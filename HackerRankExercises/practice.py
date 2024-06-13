if __name__ == '__main__':
    employees = [[1, 'John', 'HR'], [2, 'Jane', 'Engineering'], [3, 'Alice', 'HR'], [4, 'Bob', 'Engineering'], [5, 'Charlie', 'HR'], [6, 'David', 'Engineering'], [7, 'Eve', 'HR'], [8, 'Frank', 'Engineering'], [9, 'Grace', 'HR']] 
    
   
       

    hr_department = [employee[1] for employee in employees if employee[2] == 'HR']
    engineering_department = [employee[1] for employee in employees if employee[2] == 'Engineering']
    print(f'HR Department: {hr_department}')
    print(f'Engineering Department: {engineering_department}')

