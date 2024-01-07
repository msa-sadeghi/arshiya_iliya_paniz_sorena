"""
برنامه ای بنویسید که نام و نمرات سه درس یک دانش آموز را از ورودی دریاف نماید
معدلش را حساب کند
اگر معدلش از 90 بیشتر بود
A
اگر معدلش از 80 بیشتر بود
B
اگر معدلش از 70 بیشتر بود
C
اگر معدلش از 60 بیشتر بود
D
و در غیر اینصورت 
E 
را پرینت نماید

"""

name = input("enter your name: ")
score_1 = float(input('enter score number 1: '))
score_2 = float(input('enter score number 2: '))
score_3 = float(input('enter score number 3: '))

average = (score_1 + score_2 + score_3)/3

if average >= 90:
    print(f"{name}'s average is {average} and his/her grade is A")
elif average >= 80:
    print(f"{name}'s average is {average} and his/her grade is B")
elif average >= 70:
    print(f"{name}'s average is {average} and his/her grade is C")
elif average >= 60:
    print(f"{name}'s average is {average} and his/her grade is D")
else:
    print(f"{name}'s average is {average} and his/her grade is E")

input('press enter to exit ...')
