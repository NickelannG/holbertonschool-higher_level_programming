#!/usr/bin/python3
str = "abcdefghijklmnopqrstuvwxyz"
new_str = ""  # empty string
for i in range(len(str)):
    new_str += str[i]
print("{}".format(new_str))
