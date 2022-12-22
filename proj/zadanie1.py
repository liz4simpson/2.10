#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def sr_geo(*args):
    if args:
        values = [float(arg) for arg in args]
        values.sort()

        a = 1
        n = len(values)
        for i in values:
            a = a * pow(i, (1/n))
        return a
    else:
        return None


if __name__ == '__main__':
    print(sr_geo())
    print(sr_geo(1, 2, 3, 4))
    print(sr_geo(1, 5, 8, 4, 3, 9))
