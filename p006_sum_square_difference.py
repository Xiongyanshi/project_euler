#!/usr/bin/python
# _*_ coding: utf-8 _*_


def sum_square_difference(n):
    """return square of sum MINUS sum of square for numbers from 1 to n"""
    sum_of_square = 0

    for i in range(n + 1):
        sum_of_square += i**2
    print "sum of square from 1 to {} is {}".format(n, sum_of_square)

    square_of_sum = (sum(range(n + 1)))**2
    print "square of sum from 1 to {} is {}".format(n, square_of_sum)

    return square_of_sum - sum_of_square


def main():
    n = 100
    print "difference between the sum of the squares of the \
first {} natural numbers and the square of the sum \
is: {}".format(n, sum_square_difference(n))


if __name__ == '__main__':
    main()
