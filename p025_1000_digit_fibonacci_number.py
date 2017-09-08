#!/usr/bin/python
# _*_ coding: utf-8 _*_


def main():
    a = 1
    b = 1
    index = 1
    while len(str(a)) < 1000:
        # print '{} -> {}'.format(index, a)
        a, b = b, b + a
        index += 1
    return a, 'index = ', index


if __name__ == '__main__':
    print(main())
