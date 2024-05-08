#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv)
    if n == 2:
        print(f"{n-1} argument:")
        for i in range(1, n):
            print(f"{n-1}:", sys.argv[i])
    elif n == 1:
        print(f"{n-1} arguments.")
    else:
        print(f"{n-1} arguments:")
        for i in range(1, n):
            print(f"{i}:", sys.argv[i])
            i += 1
