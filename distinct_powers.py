#!/usr/bin/python
# _*_ coding: utf-8 _*_


def distinct_powers():
    min = 2
    max = 100
    power_set = set()
    for a in range(min, max + 1):
        for b in range(min, max+1):
            power_set.add(a**b)
    return len(power_set)


if __name__ == "__main__":
    print distinct_powers()
