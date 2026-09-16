age = input("Enter you age:")
new_age = int(age) + 1
print(new_age)
print(float(new_age))




print(2 + 3.5)              #implicit (done by interpreter)
print(2 + int(3.5))         #explicit  (done by programmer)


# sum

a = int(input('Enter a:'))
b = int(input('Enter b:'))
sum = a + b
print('Sum:', sum)



# # upper case, lower case
name = "Bilal Ahmed"
grade = 'A'

print(name.upper())
print(grade.lower())



# find
name = "Bilal Ahmed"
age = 21

print(name.find('al'))
print(name.find('X'))    # X is not there it will show -1 => null value (not exist)


# replace
name = "Bilal Ahmed"
grade = 'A'

print(name.replace('Ahmed', 'Gujjar'))
