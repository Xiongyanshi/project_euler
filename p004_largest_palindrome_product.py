#!/usr/bin/python
# _*_ coding: utf-8 _*_


def palindrome(n):
    """Return True if n is a palindrome, like 81133118, also works for string like"""
    n = str(n)
    for i in range(len(n) / 2):
        if n[i] != n[-1 - i]:
            return False
    return True


def largest_palindrome_product(n):
    """
    find the largest palindrome number of product of n-digit number,
    return the product of each number
    """
    max_n = int('9' * n)

    target_list = []
    max_palin = 1
    for i in range(max_n, 0, -1):
        for j in range(max_n, 0, -1):
            posedu_palindrome = i * j
            if palindrome(posedu_palindrome):
                target_list.append(posedu_palindrome)
                if posedu_palindrome > max_palin:
                    print "palindrome:{} = {} * {}".format(posedu_palindrome, i, j)
                    max_palin = posedu_palindrome

    return max(target_list)


def main():
    n = 3  # set to 3-digit number
    print "the largest palindrome made from the product of two {}-digit number is: {}".format(n, largest_palindrome_product(n))


if __name__ == '__main__':
    main()
