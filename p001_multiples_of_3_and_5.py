#!/usr/bin/python
# _*_ coding: utf-8 _*_


def multiples_of_3_and_5(n=1000):
    """return sum of all the multiples of 3 or 5 below n """
    list_3_multiples = [i * 3 for i in range(n / 3 + 1) if i * 3 < n]
    list_5_multiples = [j * 5 for j in range(n / 5 + 1) if j * 5 < n]
    return sum(set(list_3_multiples) | set(list_5_multiples))


def main():
    print '  --\nresult sum: {}\n  --'.format(multiples_of_3_and_5())


if __name__ == '__main__':
    main()
