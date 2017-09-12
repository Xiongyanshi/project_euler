#!/usr/bin/python
# _*_ coding: utf-8 _*_


def divisible_by1_to_n(a, n=20):
    """return True if a is divisible by 1 to n (defult 20)"""
    i = 2
    while i <= n:
        if a % i != 0:
            return False
        i += 1

    return True


def smallest_multiple(n=20):
    """return the smallest number be divisible by 1 to n (defult 20)"""
    i = 1
    while not divisible_by1_to_n(i, n):
        i += 1

    return i


def main():
    print 'working...'
    n = 20
    print "the smallest positive number that is evenly divisible by \
all of the numbers from 1 to {} is: {}".format(n, smallest_multiple(n))


if __name__ == '__main__':
    main()
