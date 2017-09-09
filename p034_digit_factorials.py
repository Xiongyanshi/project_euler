#!/usr/bin/python
# _*_ coding: utf-8 _*_

import math


def sum_digit_fac(n):
    '''return true if n is sum of the factorial of each digit'''
    if n == 1 or n == 2:
        return False
    result = 0
    for i in str(n):
        result += math.factorial(int(i))
    return True if result == n else False


def main():
    print 'searching digit factorial numbers...\n  --'
    summ = 0
    for i in range(50000):
        if sum_digit_fac(i):
            print 'find: {}'.format(i)
            summ += i

    print '  --\nsum is: {}\n  --'.format(summ)


if __name__ == '__main__':
    main()
