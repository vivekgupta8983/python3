#!/usr/bin/python3

import subprocess
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()

n = int(input("Enter the Number for printing Fibonacci series: "))

if (n > 0):
    print("Print a Fibonacci series up to %d " % n)
else:
    print("Please enter the valid Numbers")


fib(n)
