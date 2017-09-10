#!/usr/bin/python
# _*_ coding: utf-8 _*_

import itertools


def pandigit_nine():
    '''generator pandigital number of 0 to 9, abandon number start with zero'''
    ten_digit = itertools.permutations('0123456789', 10)
    for i in ten_digit:
        int_i = int(''.join([digit for digit in i]))
        if len(str(int_i)) == 10:
            yield int_i


def property(n):
    '''return true if n meets the property in question'''
    prime_list = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        if int(str(n)[i:i+3]) % prime_list[i-1] != 0:
            return False
    return True


def main():
    print 'searching substring divisibility numbers...\n  --'
    summ = 0
    for i in pandigit_nine():
        if property(i):
            print 'find: {}'.format(i)
            summ += int(i)
    print '  --\n sum: {}\n  --'.format(summ)


if __name__ == '__main__':
    main()
