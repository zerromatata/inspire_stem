#Program to check if a string is a palindrome
# Date : 22/02/2024
# Name : zerro matata


def isPlaindrome(s):
    return s == s[::-1]

s = "civic"
ans = isPlaindrome(s)

if ans:
    print("Yes the string you enterd is a palindrome")
else:
    print("noo the string you enterd is not a palindrome")