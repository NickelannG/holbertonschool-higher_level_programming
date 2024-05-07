#!/usr/bin/python3
n = 99
for i in range(0, n + 1):
    if i == 99:
        print("{:0>2d}".format(i))
    else:
        print("{:0>2d}, ".format(i), end="")
