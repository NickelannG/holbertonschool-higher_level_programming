#!/usr/bin/python3
str = "abcdefghijklmnopqrstuvwxyz"
new_str = ""  # empty string
for i in range(1, len(str) + 1):
    new_str += str[i - 1]
print("{}".format(new_str))
