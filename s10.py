# x = int(input("enter a number: "))
# y = int(input("enter another number: "))

# if x > y:
#     print("x is greater than y")
# elif x == y:
#     print("x and y are equal")
# else:
#     print("x is less than y")


# for i in range(5):
#     print("hello")

# for n in "python":
#     print(n)

# for x in [1,2,3,4,5,6,7,8,9]:
#     print(x)

# my_list = list()

# for i in range(4):
#     new_name = input("Enter a name: ")
#     my_list.append(new_name)

# print(my_list)


# TODO برنامه ای بنویسید که 6 عدد از ورودی دریافت نماید و هریک از اعداد را درون لیستی اضافه کند
# سپس با استفاده از لیست ایجاد شده مجموع اعداد موجود در لیست را محاسبه نمایید و نمایش دهید
# فقط از حلقه فور استفاده نمائید.


numbers = []
for i in range(6):
    a = int(input("enter a number: "))
    numbers.append(a)


print(numbers)
print(sum(numbers))