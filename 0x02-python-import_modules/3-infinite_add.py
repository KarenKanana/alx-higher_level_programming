#!/usr/bin/python3
def add_arg(argv):
    i = len(argv) - 1
    if i == 0:
        print("{:d}".format(i))
        return
    else:
        j = 1
        add = 0
        while j <= i:
            add += int(argv[j])
            j += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
