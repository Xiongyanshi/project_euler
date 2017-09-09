#!/usr/bin/python
# _*_ coding: utf-8 _*_

from prime import prime
import itertools


def pandigit(n):
    """return true if n is a pandigital number"""
    return set(str(n)) == set([str(i) for i in range(1, len(str(n)) + 1)])


def main():
    print '  --\nsearching pandigital primes...\n'
    maxn = 0
    for j in range(1, 10):
        for i in itertools.permutations(''.join([str(n)
                                                 for n in range(1, j+1)]), j):
            i_int = int(''.join(i))
            if prime(i_int):
                print '{} is pandigital prime'.format(i_int)
                if i_int > maxn:
                    maxn = i_int
    print '  --\nlargest pandigital prime is: {}\n  --'.format(maxn)


if __name__ == "__main__":
    main()
