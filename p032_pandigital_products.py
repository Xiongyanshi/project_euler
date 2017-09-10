#!/usr/bin/python
# _*_ coding: utf-8 _*_

import math


def pandigit_form(list_n):
    ''' return true if a, b, c is pandigital once from 1 to 9, a * b = c'''
    each_digit = [int(i) for j in list_n for i in str(j)]
    if set(each_digit) == set(range(1, 10)) and len(each_digit) == 9:
        print 'find: {}'.format(list_n)
        return True
    else:
        return False


def find_product(n):
    '''return the int of a * b = n'''
    result = []
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            result.append([n, i, n/i])
    return result


def pandigit_product(n):
    '''return true if n is a pandigital product'''
    for i in find_product(n):
        if pandigit_form(i):
            # print 'find: {}'.format(n)
            return True
    return False


def main():
    print 'searching pandigital products...\n  --'
    summ = 0
    for i in range(10**4):
        if pandigit_product(i):
            summ += i
    print '  --\n sum: {}\n  --'.format(summ)


if __name__ == '__main__':
    main()
