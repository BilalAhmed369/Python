age = int(input('Enter your age: '))
if age >= 18:
    print('Adult')
else:
    print('Minor')




marks = float(input('Enter your marks: '))
if marks >= 80:
    print('Grade: ', 'A')
elif marks < 80 and marks >= 60:
    print('Grade :', 'B')
elif marks < 60:
    print('Grade: ', 'C')
else:
    print('Grade :', 'F')
print("Don't loose hope, try again")