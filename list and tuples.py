
#                List --> List are built-in data types which allow us to create mutable sequence of values

marks = [98, 76, 83.5, 68, 43]
print(type(marks))
print(marks[2])
marks [1] = 70
print(marks)



student = ["Bilal", 85.5, 23, "Grw", 23]
print(student)
print(type(student))
print(student[3])



#                       checking index of a specific value from list
index = student.index(23)
print(index)



#                 slicing
fruits = ["apple", "banana", "orange", "grapes", "peach"]
print(fruits[1:3])
print(fruits[1:])
print(fruits[:3])
print(fruits[-3:])
print(fruits[-3:-2])

# checking lenght
print(len(fruits))




list = [1, 2, 3, 4, 4, 5, 6]
list.append(7)
list.sort(reverse= True)
list.insert(0, 8)          #(ind, value)
list.reverse()
list.remove(3)    #(value)
list.pop(4)             #(ind)
print(list.count(4))        # to count a number of vlaue in a list
print(list)








#                Tuple --> tuples are built-in data types which allow us to create immutable sequence of values
tup = (1, 2, 3, 4, 5, 5, 6, 7)
print(tup)
print(type(tup))



#    returs index of first occurence
print(tup.index(5))
#    returns number countns
print(tup.count(5))