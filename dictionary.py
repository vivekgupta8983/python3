#!/usr/bin/python3

#Dictionary is a collection of data which is unordered, changeable, indexed. In python it is written in curl brackets {}
# It has Key and values

car = { 'Name':'car', 'Make':'Audi', 'Year':2020, 'color':'red' }

print(car['color'])

car['cc'] = 650
print(car)

del car['Name']

print(car)