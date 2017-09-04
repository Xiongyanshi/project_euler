#!/usr/bin/python
# _*_ coding: utf-8 _*_


def power_add(a, power=4):
    if a == 0 or a == 1:
        return False
    return a == sum([int(i)**power for i in str(a)])


def main(max):
    result_list = []
    for i in range(max+1):
        if power_add(i, 5):
            print 'find:{}'.format(i)
            result_list.append(i)
    return sum(result_list)


if __name__ == '__main__':
    print('Sum Result: {}'.format(main(200000)))
