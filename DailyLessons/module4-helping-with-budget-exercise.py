spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]
high_spending = []
low_spending = []
normal_spending = []

for spending in range(len(spendings)):
    if spendings[spending] < 1000.0:
        low_spending.append(spending)
    elif spendings[spending] >= 1000.0 and spendings[spending] <= 2500.0:
        normal_spending.append(spending)
    else:
        high_spending.append(spending)
print('Numbers of months with low spendings: '+ str(len(low_spending)) +', normal spendings: ' + str(len(normal_spending)) + ', high spendings: ' + str(len(high_spending)) + '.')













