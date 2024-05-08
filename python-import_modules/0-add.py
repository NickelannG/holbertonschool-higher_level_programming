#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    added = add(a, b)
    print("{a} + {b} = {added}".format(a=1, b=2, added=add(a, b)))
