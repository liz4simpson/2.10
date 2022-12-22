#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ё
"""


def summa(*args):
    first = 0
    second = 0
    s = 0
    if args:
        for i in args:
            if i < 0:
                first = args.index(i)
                break

        for i in args:
            if i < 0 and args.index(i) > first:
                second = args.index(i)
                break

        for i in args[first+1:second:]:
            s += i
        return s

    else:
        return None


if __name__ == "__main__":
    print(summa())
    print(summa(1, 2, -3, 3, 4, 1, -5, 3,))
