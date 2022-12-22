#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Даны баллы за экзамен студентов в виде ключ-значения, определить средний балл и самый высокий балл среди всех студентов.
"""


def marks(**scores):
    n = len(scores)
    maxi = 0
    summa = 0
    for kw in scores:
        summa = summa + scores[kw]
        sr_arf = summa / n
        if scores[kw] > maxi:
            maxi = scores[kw]
    print("Лучший балл в группе:", maxi)
    print("Средний балл среди всех студентов - ", sr_arf)


if __name__ == "__main__":
    marks(
        Миша=60,
        Саша=70,
        Оля=86,
        Коля=30,
        Вова=87,
    )
