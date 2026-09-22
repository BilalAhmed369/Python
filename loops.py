
# range -> (start, stop, step)



range
num = range(5)
print(num)





                       # while loop

# 1 to 10
count = 1
while count <= 10:
    print(count)
    count += 1



# 10 to 1
count = 10
while count >= 1:
    print(count)
    count -= 1



# num = int(input("Enter the num: "))
while num >=0:
    print(num)
    num -=1



# print even numbers
num = 2
while num <= 20:
    print(num)
    num += 2



# print odd numbers
num = 1
while num <= 20:
    print(num)
    num += 2



# checking password
password = input("Enter you password: ")
while password != "python123":
    print("Wrong password:")
    password = input("Enter your password again: ")

print("Granted")



# multiplication
i = 1
while i <= 10:
    print(i * 5)
    i += 1



                       # for loop


for i in range(10):
    print(i)



num = range(10)
for i in num:
    print(i)



for i in range(0, 5001):
    print(i)




for i in range(1, 21):
    if i % 2 == 0:
        print(i)




                     # break and continue
for i in range(1, 61):
    if i == 51:
        break
    if i % 3 == 0:
        print(i)



for i in range(1, 31):
    if i == 21:
        continue
    if i % 3 == 0:
        print(i)