import random

freq_1 = 0
freq_2 = 0
freq_3 = 0
freq_4 = 0
freq_5 = 0
freq_6 = 0

for _ in range(100):
    face = random.randint(1,6)
    if face == 1:
        freq_1 += 1
    elif face == 2:
        freq_2 += 1

print(f"number of 1 {freq_1}")
print(f"number of 2 {freq_2}")

#TODO 
# welcome to python class. we are going to learn everythings about python.
# در متن بالا تعداد کاراکتر 
# o
# را نمایش دهید