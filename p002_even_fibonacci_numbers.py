#!/usr/bin/python
# _*_ coding: utf-8 _*_


def fibonacci(max_n):
    """Return a list contain fibonacci numbers below max_n"""
    fib_list = [1, 1]
    while fib_list[-1] + fib_list[-2] < max_n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


def even_fibonacci(max_num):
    """return a list consist of even fibonacci below max_num"""
    fib_list = fibonacci(max_num)
    even_dib_list = []

    for i in fib_list:
        if i % 2 == 0:
            print "even fibonacci number: {}".format(i)
            even_dib_list.append(i)

    return even_dib_list


def main():
    n = 4 * (10**6)
    print "the sum of even fibonacci number below {} is: {}".format(n, sum(even_fibonacci(n)))


if __name__ == '__main__':
    main()
