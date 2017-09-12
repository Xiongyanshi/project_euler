#!/usr/bin/python
# _*_ coding: utf-8 _*_


def main():
    summ = 0
    for i in range(1, 1001):
        summ += i**i
    print '  --\nlast ten digits is: {}\n  --'.format(str(summ)[-10:])


if __name__ == '__main__':
    main()
