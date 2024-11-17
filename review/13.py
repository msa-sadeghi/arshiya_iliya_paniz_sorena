# try:
#     x = int(input("enter a number: "))
#     y = int(input("enter a number: "))

#     print(x/y)
# except ValueError:
#     print("you must enter valid number")
# except ZeroDivisionError:
#     print("can not divide number by zero")
# try:
#     print(x)
# except NameError:
#     print("blalalal")

# try:
#     f = open("python.txt", "r")
# except FileNotFoundError:
#     print("file not found")
# else:
#     print('no error')
# finally:
#     print("finally")
#     f.close()


# x = {
#     "python" : 20,
#     "js" : 40,
#     "django":60
# }

# try:
#     x["python"]+= 1
#     print(x)
#     course_name = "react"
#     x["react"] += 1
# except KeyError:
#     print("course name is not valid")


import math
try:
    print(math.sqrt(-4))
except ValueError:
    print("blalal")