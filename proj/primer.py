#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def median(*args):
    if args:
        values = [float(arg) for arg in args]
        values.sort()

        n = len(values)
        idx = n//2
        if n % 2:
            return values[idx]
        else:
            return (values[idx] + values[idx-1]) / 2

    else:
        return None


if __name__ == '__main__':
    print(median())
    print(median(3, 7, 1, 6, 9))
    print(median(1, 5, 8, 4, 3, 9))

