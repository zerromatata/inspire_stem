laptop = {"make":"lenovo","colour":"black","weight":"1.4","year":"2021"}


print(laptop["make"])
print(laptop["colour"])
print(laptop["year"])

#to change values 
laptop["colour"] = "red"
laptop["year"] ="2023"


print(laptop)

laptop["size"] = "1980 x 1200"

print(laptop)

del laptop["colour"]
print(laptop)
"""

"""

for key,value in laptop.items():
    print(key)
    print("\n")
    print(value)