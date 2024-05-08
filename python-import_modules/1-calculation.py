#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add, sub, mul, div
    added = add(a, b)
    subbed = sub(a, b)
    product = mul(a, b)
    divided = div(a, b)
    print("{} + {} = {}".format(a, b, added))
    print("{} - {} = {}".format(a, b, subbed))
    print("{} * {} = {}".format(a, b, product))
    print("{} / {} = {:.0f}".format(a, b, divided))
