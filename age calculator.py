#!/usr/bin/python3

from datetime import datetime, date

name = input("Enter your Name: ")
print("Hello %s Enter your DOB in these format (dd/mm/yyyy)" % name)
date_of_birth = datetime.strptime(input("--->"), "%d/%m/%Y")

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = calculate_age(date_of_birth)

print("Hi %s your are %d Years old" % (name, age))