#!/usr/bin/python3

list = ["ghee", "eggs", "milk", "curd", "fruits", "vegs"]

for i in list:
    if i == "eggs":
        print("I not going to buy " + i)
        continue
    print("I am buying " +i)
