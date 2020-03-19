#!/usr/bin/python3

num = "1,123,1234,123445,123,123,56,767,87,9"

clnnum = ""

for i in range(0, len(num)):
    if num [i] in "123456789":
        clnnum1 = clnnum + num[i]
        clnnum += num[i]          # augument assignment
print(clnnum1)
print(clnnum)