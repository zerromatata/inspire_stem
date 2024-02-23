# this is a program to generate the terms and sum in the geometric progression
# date : 20/2/2024
# name : zerro

a =int(input("enter first term: "))
r = int(input("enter the common ration:"))
n = int(input("enter the number of the terms:"))

t = (a * r **(n - 1))
print("the next number is equal to: ",t)