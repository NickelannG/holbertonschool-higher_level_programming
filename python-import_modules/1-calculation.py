#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add
    added = a + b
    print("{} + {} = {}".format(a, b, added))

    from calculator_1 import sub
    subbed = a - b
    print("{} - {} = {}".format(a, b, subbed))

    from calculator_1 import mul
    product = a * b
    print("{} * {} = {}".format(a, b, product))

    from calculator_1 import div
    divided = a / b
    print("{} / {} = {:.0f}".format(a, b, divided))
