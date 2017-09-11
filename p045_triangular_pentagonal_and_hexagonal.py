#!/usr/bin/python
# _*_ coding: utf-8 _*_


def tri(n):
    '''return n-th triangular number'''
    return n*(n + 1) / 2


def pen(n):
    '''return n-th pentagonal number'''
    return n*(3*n - 1) / 2


def hexa(n):
    '''return n-th hexagonal number'''
    return n*(2*n - 1)


def main():
    print 'searching...'
    tri_set = set()
    pen_set = set()
    hex_set = set()
    i = 1
    common_item = []
    while len(common_item) < 3:
        tri_set.add(tri(i))
        pen_set.add(pen(i))
        hex_set.add(hexa(i))
        common_item = [item for item in tri_set & pen_set & hex_set]
        i += 1
    print '  --\nresult: {}\n  --'.format(common_item[-1])


if __name__ == '__main__':
    main()
