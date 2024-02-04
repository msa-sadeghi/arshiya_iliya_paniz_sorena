# numbers = [1,2,45,67,89,90]

# total = 0
# count = 0

# for n in numbers:
#     if n % 2 != 0:
#         print(n)
#         count += 1
#         total += n
        
# print(total, count)

numbers = [1,2,45,67,89,90]
count = 0
for x in numbers:
    if len(str(x)) == 2:
        print(x)
        count += 1
        
print(count)
    
