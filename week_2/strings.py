# strings in python
# Date : 22/02/2024
# Name : zerro


city = "nairobi"

print(city[0])# n
print(city[1])# a
print(city[2])# i
print(city[3])# r
print(city[-2])# o
print(city[5])# b
print(city[6])# i

# convert to upper case


print(city)
print("\n\n") # prints new line
print(city.upper())
name = "ZERRO MATATA"
print(name)
print(name.lower()) # this converts string to lowercase

town = ("    Naivasha    ")
print(town)
print("\t") # new tab
print(town.strip())

f_name = "Zerro"
s_name = "matata"

full_name = f_name + s_name
print(full_name)

# replacing character

fruit ="orangeooooo"
print(fruit.replace('o','y'))

subject = "physical,Sciences"
print(subject.split(":"))


age = 35
height = 1.2
print("I am {0}years old and {1}meters tall" .format(age , height))

