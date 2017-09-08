#!/usr/bin/python
# _*_ coding: utf-8 _*_


def pandigit(n, m=9):
    """Return True if n is a pandigit number of 1-9, like 918273645"""
    return len(str(n)) == 9 and \
        set([str(i) for i in range(1, m+1)]) == set(str(n))


def con_pro(i, n):
    """Return concatenated product of integer i and (1,2...n), n > 1"""
    result = []
    for each in range(1, n+1):
        result.append(str(i*each))
    return int(''.join(result))


def main():
    print 'searching qualified 9 digit numbers....\n  --'
    max_n = 0
    for i in range(1, 10000):
        for j in range(1, 10):
            concat = con_pro(i, j)
            if pandigit(concat):
                print '{} = {} * {}'.format(concat, i, range(1, j+1))
                max_n = concat
    print '  --\n max one is:{}\n  --'.format(max_n)


if __name__ == "__main__":
    main()
    print '-- good bye! --'
