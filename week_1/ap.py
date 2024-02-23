#program to determine the arithmetic progression of sequences
# date : 20/2/2024
# name :zerro

a = int(input("enter the first term"))
d = int(input("enter the common difference"))
n = int(input("enter the number of terms"))

nth_term = (a +(d - 1) * n)
print("the next number is equal to :", nth_term)

