# x = [1.1, 1.2,1.11,22,5,6,0,12]
# x.sort()
# print(x)
# x.sort(reverse=True)
# print(x)
# my_list = []
# for i in range(6):
#     name = input("enter a name: ")
#     if name[0] == "a" or name[0] == "A":
#         my_list.append(name)
        
# print(my_list)

# heights = []
# for i in range(5):
#     h = float(input("enter a height: "))
#     if 170 < h < 180:
#         heights.append(h)
# print(len(heights))
        



# my_string = input("enter a message:> ")
# my_char = input("enter a character:> ")
# if my_char in my_string:
#     print("ok")
# else:
#     print("not ok")

# names = ()
# for i in range(4):
#     x = input("enter a name:> ")
#     names += (x,)
# largest_name = ""
# for n in names:
#     if len(n) > len(largest_name):
#         largest_name = n
# print(largest_name)



# names = []

# for i in range(5):
#     n = input("enter a name:> ")
#     names.append(n)
#     if len(n) > 3:
#         print(tuple(n))
# اعداد = []
# for تکرار in range(4):
#     عدد = int(input("enter a number:> "))
#     اعداد.append(عدد)
    
# مجموع_اعداد_زوج = 0
# for عدد in اعداد:
#     if عدد % 2 == 0:
#         مجموع_اعداد_زوج += عدد
        
# print(مجموع_اعداد_زوج)
        
        
اسم = input("enter a name:> ")
print(اسم[-1::-1])

for i in range(len(اسم)-1, -1, -1):
    print(اسم[i], end="")