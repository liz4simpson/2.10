#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def sr_garm(*args):
    if args:
        values = [float(arg) for arg in args]
        values.sort()

        a = 0
        n = len(values)
        for i in values:
            a += (1 / i)
        h = n / a
        return h
    else:
        return None


if __name__ == '__main__':
    print(sr_garm())
    print(sr_garm(1, 2, 3, 4))
    print(sr_garm(1, 5, 8, 4, 3, 9))
