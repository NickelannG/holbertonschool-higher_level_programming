#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    added = a + b
    subbed = a - b
    product = a * b
    divided = a / b
    from calculator_1 import add, sub, mul, div
    print("{} + {} = {}".format(a, b, added))
    print("{} - {} = {}".format(a, b, subbed))
    print("{} * {} = {}".format(a, b, product))
    print("{} / {} = {:.0f}".format(a, b, divided))
