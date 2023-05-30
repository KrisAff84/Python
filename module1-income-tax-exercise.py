income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43
# My solution
print (f'Your income is {income} and you would pay {income * lowtaxland_rate} income') 
print (f'tax in Lowtaxland or {income * ripoffland_rate} income tax in Ripoffland.')
print (f'You would save {(income * ripoffland_rate) - (income * lowtaxland_rate)} by paying taxes in Lowtaxland!')
print ()
print ()
# Given solution
print('Your income is', income, 'and you would pay', income * lowtaxland_rate, 'income tax in Lowtaxland or', income * ripoffland_rate, 'income tax in Ripoffland. You would save', income * ripoffland_rate - income * lowtaxland_rate, 'by paying taxes in Lowtaxland!')
