#!/usr/bin/python3
n = 100
for i in range(1, n + 2):
    if (i % 3) == 0 and (i % 5) == 0:
        print("FizzBuzz ", end="")
    elif (i % 3) == 0:
        print("Fizz ", end="")
    elif (i % 5) == 0:
        print("Buzz ", end="")
    elif i == 101:
        print("$")
    else:
        print(i, " ", end="")
