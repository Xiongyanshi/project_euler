#!/usr/bin/python
# _*_ coding: utf-8 _*_

from prime import prime


def truncate_list_left(n):
    """Return list of truncated numbers of n from left"""
    n_list = [i for i in str(n)]
    left_list = []
    while n_list:
        left_list.append(int(''.join(n_list)))
        n_list = n_list[1:]
    return left_list


def truncate_list_right(n):
    """Return list of truncated numbers of n from right"""
    n_list = [i for i in str(n)]
    right_list = []
    while n_list:
        right_list.append(int(''.join(n_list)))
        n_list = n_list[:-1]
    return right_list


def prime_truncate_left_right(n):
    truncate_list = list(set(truncate_list_left(n) + truncate_list_right(n)))
    for i in truncate_list:
        if not prime(i):
            return False
    return True


def main():
    print 'searching 11 truncate primes:\n  --'
    count = 0
    summ = 0
    i = 10
    while count < 11:
        if prime_truncate_left_right(i):
            count += 1
            summ += i
            print '{0}-th: \t{1}'.format(count, i)
        i += 1
    print '  --\n sum:{0}\n  --'.format(summ)


if __name__ == "__main__":
    main()
