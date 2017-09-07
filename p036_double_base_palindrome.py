#!/usr/bin/python
# _*_ coding: utf-8 _*_


def palindrome_base_ten(n):
    """Return True if n is a palindromic number in base ten, like 14541"""
    n = str(n)
    for i in range(len(n)/2):
        if n[i] != n[-1 - i]:
            return False
    return True


def palindrome_base_two(n):
    """Return True if n is a palindromic number in base two,
    like 585 = ob1001001001"""

    n = bin(n)[2:]
    return palindrome_base_ten(n)


def main():
    sum = 0
    for i in range(1, 10**6):
        if palindrome_base_ten(i) and palindrome_base_two(i):
            print 'find: {0} \t {1}'.format(i, bin(i)[2:])
            sum += i
    print ' --\nsum: {0}\n --'.format(sum)


if __name__ == "__main__":
    main()
